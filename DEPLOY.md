# SheerID Auto-Verification Bot - Deployment Guide

This document details how to deploy the SheerID Auto-Verification Telegram Bot.

---

## 📋 Table of Contents

1. [System Requirements](#system-requirements)
2. [Quick Deployment](#quick-deployment)
3. [Docker Deployment](#docker-deployment)
4. [Manual Deployment](#manual-deployment)
5. [Configuration](#configuration)
6. [Troubleshooting](#troubleshooting)
7. [Maintenance and Updates](#maintenance-and-updates)

---

## 🔧 System Requirements

### Minimum Configuration

- **Operating System**: Linux (Ubuntu 20.04+ recommended) / Windows 10+ / macOS 10.15+
- **Python**: 3.11 or higher
- **MySQL**: 5.7 or higher
- **Memory**: 512MB RAM (1GB+ recommended)
- **Disk Space**: 2GB+
- **Network**: Stable internet connection

### Recommended Configuration

- **Operating System**: Ubuntu 22.04 LTS
- **Python**: 3.11
- **MySQL**: 8.0
- **Memory**: 2GB+ RAM
- **Disk Space**: 5GB+
- **Network**: 10Mbps+ bandwidth

---

## 🚀 Quick Deployment

### Using Docker Compose (Simplest)

```bash
# 1. Clone repository
git clone https://github.com/PastKing/tgbot-verify.git
cd tgbot-verify

# 2. Configure environment variables
cp env.example .env
nano .env  # Fill in your configuration

# 3. Start services
docker-compose up -d

# 4. View logs
docker-compose logs -f

# 5. Stop services
docker-compose down
```

Done! The bot should now be running.

---

## 🐳 Docker Deployment

### Method 1: Using Docker Compose (Recommended)

#### 1. Prepare Configuration File

Create `.env` file:

```env
# Telegram Bot Configuration
BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrsTUVwxyz
CHANNEL_USERNAME=pk_oa
CHANNEL_URL=https://t.me/pk_oa
ADMIN_USER_ID=123456789

# MySQL Database Configuration
MYSQL_HOST=your_mysql_host
MYSQL_PORT=3306
MYSQL_USER=tgbot_user
MYSQL_PASSWORD=your_secure_password
MYSQL_DATABASE=tgbot_verify
```

#### 2. Start Services

```bash
docker-compose up -d
```

#### 3. Check Status

```bash
# Check container status
docker-compose ps

# View real-time logs
docker-compose logs -f

# View last 50 lines of logs
docker-compose logs --tail=50
```

#### 4. Restart Services

```bash
# Restart all services
docker-compose restart

# Restart single service
docker-compose restart tgbot
```

#### 5. Update Code

```bash
# Pull latest code
git pull

# Rebuild and start
docker-compose up -d --build
```

### Method 2: Manual Docker Deployment

```bash
# 1. Build image
docker build -t tgbot-verify:latest .

# 2. Run container
docker run -d \
  --name tgbot-verify \
  --restart unless-stopped \
  --env-file .env \
  -v $(pwd)/logs:/app/logs \
  tgbot-verify:latest

# 3. View logs
docker logs -f tgbot-verify

# 4. Stop container
docker stop tgbot-verify

# 5. Remove container
docker rm tgbot-verify
```

---

## 🔨 Manual Deployment

### Linux / macOS

#### 1. Install Dependencies

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install -y python3.11 python3.11-pip python3.11-venv mysql-server

# macOS (using Homebrew)
brew install python@3.11 mysql
```

#### 2. Create Virtual Environment

```bash
python3.11 -m venv venv
source venv/bin/activate  # Linux/macOS
```

#### 3. Install Python Packages

```bash
pip install --upgrade pip
pip install -r requirements.txt
playwright install chromium
```

#### 4. Configure Database

```bash
# Login to MySQL
mysql -u root -p

# Create database and user
CREATE DATABASE tgbot_verify CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'tgbot_user'@'localhost' IDENTIFIED BY 'your_secure_password';
GRANT ALL PRIVILEGES ON tgbot_verify.* TO 'tgbot_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

#### 5. Configure Environment Variables

```bash
cp env.example .env
nano .env  # Edit configuration
```

#### 6. Start Bot

```bash
# Run in foreground (for testing)
python bot.py

# Run in background (using nohup)
nohup python bot.py > bot.log 2>&1 &

# Run in background (using screen)
screen -S tgbot
python bot.py
# Ctrl+A+D to exit screen
# screen -r tgbot to reconnect
```

### Windows

#### 1. Install Dependencies

- Download and install [Python 3.11+](https://www.python.org/downloads/)
- Download and install [MySQL](https://dev.mysql.com/downloads/installer/)

#### 2. Create Virtual Environment

```cmd
python -m venv venv
venv\Scripts\activate
```

#### 3. Install Python Packages

```cmd
pip install --upgrade pip
pip install -r requirements.txt
playwright install chromium
```

#### 4. Configure Database

Use MySQL Workbench or command line to create the database.

#### 5. Configure Environment Variables

Copy `env.example` to `.env` and edit it.

#### 6. Start Bot

```cmd
python bot.py
```

---

## ⚙️ Configuration

### Environment Variables Explained

#### Telegram Configuration

```env
# Bot Token (Required)
# Obtain from @BotFather
BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrsTUVwxyz

# Channel username (Optional)
# No @ symbol needed
CHANNEL_USERNAME=pk_oa

# Channel link (Optional)
CHANNEL_URL=https://t.me/pk_oa

# Admin Telegram ID (Required)
# Can be obtained from @userinfobot
ADMIN_USER_ID=123456789
```

#### MySQL Configuration

```env
# Database host (Required)
MYSQL_HOST=localhost         # Local deployment
# MYSQL_HOST=192.168.1.100  # Remote database
# MYSQL_HOST=mysql          # Docker Compose

# Database port (Optional, default 3306)
MYSQL_PORT=3306

# Database username (Required)
MYSQL_USER=tgbot_user

# Database password (Required)
MYSQL_PASSWORD=your_secure_password

# Database name (Required)
MYSQL_DATABASE=tgbot_verify
```

### Points System Configuration

Modify in `config.py`:

```python
# Points configuration
VERIFY_COST = 1        # Points cost for verification
CHECKIN_REWARD = 1     # Check-in reward points
INVITE_REWARD = 2      # Invitation reward points
REGISTER_REWARD = 1    # Registration reward points
```

### Concurrency Control

Adjust in `utils/concurrency.py`:

```python
# Auto-calculate based on system resources
_base_concurrency = _calculate_max_concurrency()

# Concurrency limit for each verification type
_verification_semaphores = {
    "gemini_one_pro": Semaphore(_base_concurrency // 5),
    "chatgpt_teacher_k12": Semaphore(_base_concurrency // 5),
    "spotify_student": Semaphore(_base_concurrency // 5),
    "youtube_student": Semaphore(_base_concurrency // 5),
    "bolt_teacher": Semaphore(_base_concurrency // 5),
}
```

---

## 🔍 Troubleshooting

### 1. Invalid Bot Token

**Issue**: `telegram.error.InvalidToken: The token was rejected by the server.`

**Solution**:
- Check if `BOT_TOKEN` in `.env` file is correct
- Ensure there are no extra spaces or quotes
- Get a new token from @BotFather

### 2. Database Connection Failed

**Issue**: `pymysql.err.OperationalError: (2003, "Can't connect to MySQL server")`

**Solution**:
- Check if MySQL service is running: `systemctl status mysql`
- Verify database configuration is correct
- Check firewall settings
- Confirm database user permissions

### 3. Playwright Browser Installation Failed

**Issue**: `playwright._impl._api_types.Error: Executable doesn't exist`

**Solution**:
```bash
playwright install chromium
# Or install all dependencies
playwright install-deps chromium
```

### 4. Port Already in Use

**Issue**: Docker container cannot start, port conflict

**Solution**:
```bash
# Check port usage
netstat -tlnp | grep :3306
# Modify port mapping in docker-compose.yml
```

### 5. Out of Memory

**Issue**: Server runs out of memory causing crashes

**Solution**:
- Increase server memory
- Reduce concurrency limit
- Enable swap space:
```bash
sudo fallocate -l 2G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```

### 6. Log Files Too Large

**Issue**: Log files consume excessive disk space

**Solution**:
- Docker automatically limits log size (see `docker-compose.yml`)
- Manual cleanup: `truncate -s 0 logs/*.log`
- Set up log rotation

---

## 🔄 Maintenance and Updates

### View Logs

```bash
# Docker Compose
docker-compose logs -f --tail=100

# Manual deployment
tail -f bot.log
tail -f logs/bot.log
```

### Backup Database

```bash
# Full backup
mysqldump -u tgbot_user -p tgbot_verify > backup_$(date +%Y%m%d).sql

# Data-only backup
mysqldump -u tgbot_user -p --no-create-info tgbot_verify > data_backup.sql

# Restore backup
mysql -u tgbot_user -p tgbot_verify < backup.sql
```

### Update Code

```bash
# Pull latest code
git pull origin main

# Docker deployment
docker-compose down
docker-compose up -d --build

# Manual deployment
source venv/bin/activate
pip install -r requirements.txt
python bot.py
```

### Monitor Running Status

#### Using systemd (Recommended for Linux)

Create service file `/etc/systemd/system/tgbot-verify.service`:

```ini
[Unit]
Description=SheerID Telegram Verification Bot
After=network.target mysql.service

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/path/to/tgbot-verify
ExecStart=/path/to/tgbot-verify/venv/bin/python bot.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Start service:

```bash
sudo systemctl daemon-reload
sudo systemctl enable tgbot-verify
sudo systemctl start tgbot-verify
sudo systemctl status tgbot-verify
```

#### Using supervisor

Install supervisor:

```bash
sudo apt install supervisor
```

Create configuration file `/etc/supervisor/conf.d/tgbot-verify.conf`:

```ini
[program:tgbot-verify]
directory=/path/to/tgbot-verify
command=/path/to/tgbot-verify/venv/bin/python bot.py
autostart=true
autorestart=true
stderr_logfile=/var/log/tgbot-verify.err.log
stdout_logfile=/var/log/tgbot-verify.out.log
user=ubuntu
```

Start:

```bash
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start tgbot-verify
```

---

## 🔒 Security Recommendations

1. **Use Strong Passwords**
   - Rotate Bot Token regularly
   - Database password at least 16 characters
   - Don't use default passwords

2. **Restrict Database Access**
   ```sql
   # Allow only local connections
   CREATE USER 'tgbot_user'@'localhost' IDENTIFIED BY 'password';
   
   # Allow specific IP
   CREATE USER 'tgbot_user'@'192.168.1.100' IDENTIFIED BY 'password';
   ```

3. **Configure Firewall**
   ```bash
   # Only open necessary ports
   sudo ufw allow 22/tcp      # SSH
   sudo ufw enable
   ```

4. **Regular Updates**
   ```bash
   sudo apt update && sudo apt upgrade
   pip install --upgrade -r requirements.txt
   ```

5. **Backup Strategy**
   - Auto-backup database daily
   - Keep at least 7 days of backups
   - Regularly test restore process

---

## 📞 Technical Support

- 📺 Telegram Channel: https://t.me/pk_oa
- 🐛 Issue Tracking: [GitHub Issues](https://github.com/PastKing/tgbot-verify/issues)

---

<p align="center">
  <strong>Happy Deploying!</strong>
</p>

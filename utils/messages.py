"""Message templates"""
from config import CHANNEL_URL, VERIFY_COST, HELP_NOTION_URL


def get_welcome_message(full_name: str, invited_by: bool = False) -> str:
    """Get welcome message"""
    msg = (
        f"🎉 Welcome, {full_name}!\n"
        "You have successfully registered and received 1 point.\n"
    )
    if invited_by:
        msg += "Thank you for joining through an invitation link, the inviter has received 2 points.\n"

    msg += (
        "\nThis bot can automatically complete SheerID verification.\n"
        "Quick start:\n"
        "/about - Learn about bot features\n"
        "/balance - Check points balance\n"
        "/help - View complete command list\n\n"
        "Earn more points:\n"
        "/qd - Daily check-in\n"
        "/invite - Invite friends\n"
        f"Join channel: {CHANNEL_URL}"
    )
    return msg


def get_about_message() -> str:
    """Get about message"""
    return (
        "🤖 SheerID Auto-Verification Bot\n"
        "\n"
        "Features:\n"
        "- Automatically complete SheerID student/teacher verification\n"
        "- Supports Gemini One Pro, ChatGPT Teacher K12, Spotify Student, YouTube Student, Bolt.new Teacher verification\n"
        "\n"
        "Earning points:\n"
        "- Registration bonus: 1 point\n"
        "- Daily check-in: +1 point\n"
        "- Invite friends: +2 points per person\n"
        "- Redeem codes (per code rules)\n"
        f"- Join channel: {CHANNEL_URL}\n"
        "\n"
        "How to use:\n"
        "1. Start verification on the website and copy the complete verification link\n"
        "2. Send /verify, /verify2, /verify3, /verify4, or /verify5 with the link\n"
        "3. Wait for processing and check results\n"
        "4. Bolt.new verification automatically retrieves code, use /getV4Code <verification_id> to manually query\n"
        "\n"
        "For more commands, send /help"
    )


def get_help_message(is_admin: bool = False) -> str:
    """Get help message"""
    msg = (
        "📖 SheerID Auto-Verification Bot - Help\n"
        "\n"
        "User Commands:\n"
        "/start - Start using (register)\n"
        "/about - Learn about bot features\n"
        "/balance - Check points balance\n"
        "/qd - Daily check-in (+1 point)\n"
        "/invite - Generate invitation link (+2 points per person)\n"
        "/use <code> - Redeem points with code\n"
        f"/verify <link> - Gemini One Pro verification (-{VERIFY_COST} points)\n"
        f"/verify2 <link> - ChatGPT Teacher K12 verification (-{VERIFY_COST} points)\n"
        f"/verify3 <link> - Spotify Student verification (-{VERIFY_COST} points)\n"
        f"/verify4 <link> - Bolt.new Teacher verification (-{VERIFY_COST} points)\n"
        f"/verify5 <link> - YouTube Student Premium verification (-{VERIFY_COST} points)\n"
        "/getV4Code <verification_id> - Get Bolt.new verification code\n"
        "/help - View this help information\n"
        f"Verification failure help: {HELP_NOTION_URL}\n"
    )

    if is_admin:
        msg += (
            "\nAdmin Commands:\n"
            "/addbalance <user_id> <points> - Add user points\n"
            "/block <user_id> - Block user\n"
            "/white <user_id> - Unblock user\n"
            "/blacklist - View blacklist\n"
            "/genkey <code> <points> [times] [days] - Generate redemption code\n"
            "/listkeys - View redemption code list\n"
            "/broadcast <text> - Broadcast notification to all users\n"
        )

    return msg


def get_insufficient_balance_message(current_balance: int) -> str:
    """Get insufficient balance message"""
    return (
        f"Insufficient points! Need {VERIFY_COST} points, you have {current_balance} points.\n\n"
        "Ways to earn points:\n"
        "- Daily check-in /qd\n"
        "- Invite friends /invite\n"
        "- Redeem code /use <code>"
    )


def get_verify_usage_message(command: str, service_name: str) -> str:
    """Get verification command usage message"""
    return (
        f"Usage: {command} <SheerID link>\n\n"
        "Example:\n"
        f"{command} https://services.sheerid.com/verify/xxx/?verificationId=xxx\n\n"
        "Get verification link:\n"
        f"1. Visit {service_name} verification page\n"
        "2. Start verification process\n"
        "3. Copy the complete URL from browser address bar\n"
        f"4. Submit using {command} command"
    )

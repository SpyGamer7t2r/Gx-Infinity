def apply_ai_mode(message: str, mode: str) -> str:
    if not message:
        return "🤖 Kya bolu main? Message hi nahi mila."

    mode = mode.lower()

    if mode == "romantic":
        return f"❤️ Baby, suno na... {message} 😘"
    elif mode == "savage":
        return f"😈 Oye sun {message}, tu soch bhi kaise liya? 💀"
    elif mode == "jugaadu":
        return f"😏 Arre bhai simple hai... {message}, kaam ho jaayega!"
    elif mode == "funny":
        return f"😂 Abe oye! {message} lagta hai tu comedy ka baap hai!"
    elif mode == "serious":
        return f"🧠 Let's be logical here: {message}"
    else:
        return f"🧍‍♂️ {message}"  # Default mode

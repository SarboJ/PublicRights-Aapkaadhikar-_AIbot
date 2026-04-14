def map_legal_sections(issue: str):
    issue = issue.lower()

    ipc, crpc, cpc, consumer = [], [], [], []

    # IPC
    if "fraud" in issue or "cheat" in issue:
        ipc.append("Section 420 – Cheating")
    if "threat" in issue:
        ipc.append("Section 506 – Criminal Intimidation")

    # CrPC
    if "police" in issue or "fir" in issue:
        crpc.append("Section 154 – FIR registration")
    if "arrest" in issue:
        crpc.append("Section 41 – Arrest")

    # CPC
    if "property" in issue or "civil" in issue:
        cpc.append("Section 9 – Civil court jurisdiction")
    if "injunction" in issue:
        cpc.append("Order 39 – Temporary injunction")

    # Consumer Law
    if "defective" in issue or "product" in issue:
        consumer.append("Deficiency in service – Consumer Protection Act")
    if "refund" in issue:
        consumer.append("Right to refund – Consumer Protection Act")

    return {
        "ipc": ipc,
        "crpc": crpc,
        "cpc": cpc,
        "consumer": consumer
    }


def extract_notice_fields(text: str):
    laws = map_legal_sections(text)

    return {
        "sender": "PublicRights User",
        "receiver": "Opposite Party",
        "subject": "Legal Notice",
        "issue": text,
        "demand": "resolve the matter",
        "timeline": "15",
        "laws": laws
    }

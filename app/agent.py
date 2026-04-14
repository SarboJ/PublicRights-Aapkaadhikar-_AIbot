def extract_notice_fields(text: str):
    laws = map_legal_sections(text)
def map_legal_sections(issue: str):
    issue = issue.lower()

    ipc = []
    crpc = []
    cpc = []
    consumer = []

    # ---------------- IPC ----------------
    if "cheat" in issue or "fraud" in issue:
        ipc.append("Section 420 – Cheating")

    if "threat" in issue:
        ipc.append("Section 506 – Criminal Intimidation")

    if "theft" in issue:
        ipc.append("Section 378 – Theft")

    # ---------------- CrPC ----------------
    if "police" in issue or "complaint" in issue or "fir" in issue:
        crpc.append("Section 154 – FIR registration")

    if "arrest" in issue:
        crpc.append("Section 41 – Arrest without warrant")

    if "investigation" in issue:
        crpc.append("Section 156 – Police investigation powers")

    # ---------------- CPC ----------------
    if "civil suit" in issue or "property dispute" in issue:
        cpc.append("Section 9 – Jurisdiction of civil courts")

    if "injunction" in issue:
        cpc.append("Order 39 – Temporary injunction")

    if "notice before suit" in issue or "government case" in issue:
        cpc.append("Section 80 – Notice to government")

    # ---------------- Consumer Law ----------------
    if "defective product" in issue or "bad service" in issue:
        consumer.append("Consumer Protection Act – Deficiency in service")

    if "refund" in issue or "ecommerce" in issue:
        consumer.append("Right to refund under Consumer Protection Act")

    if "unfair trade" in issue:
        consumer.append("Unfair Trade Practice – Consumer Protection Act")

    return {
        "ipc": ipc,
        "crpc": crpc,
        "cpc": cpc,
        "consumer": consumer,
        "sender": "PublicRights User",
        "receiver": "Opposite Party",
        "subject": "Legal Notice",
        "issue": text,
        "demand": "resolve the matter and compensate losses",
        "timeline": "15"
    }
    return   {
        "sender": "PublicRights User",
        "receiver": "Opposite Party",
        "subject": "Legal Notice",
        "issue": text,
        "demand": "resolve the matter and compensate losses",
        "timeline": "15",
        "laws": laws
    }

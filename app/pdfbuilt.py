from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime

def format_law_section(title, sections):
    if not sections:
        return ""
    text = f"<b>{title}:</b><br/>"
    for sec in sections:
        text += f"• {sec}<br/>"
    return text


def generate_legal_notice(data, file_path="notice.pdf"):
    doc = SimpleDocTemplate(file_path)
    styles = getSampleStyleSheet()
    content = []

    content.append(Paragraph("<b>LEGAL NOTICE</b>", styles["Title"]))
    content.append(Spacer(1, 12))

    content.append(Paragraph(f"Date: {datetime.now().strftime('%d %B %Y')}", styles["Normal"]))
    content.append(Spacer(1, 12))

    content.append(Paragraph(f"<b>From:</b> {data['sender']}", styles["Normal"]))
    content.append(Paragraph(f"<b>To:</b> {data['receiver']}", styles["Normal"]))
    content.append(Spacer(1, 12))

    content.append(Paragraph(f"<b>Subject:</b> {data['subject']}", styles["Normal"]))
    content.append(Spacer(1, 12))

    body = f"""
    Under instructions from my client, I hereby issue this legal notice:

    1. That the matter concerns: {data['issue']}.
    2. That your actions are unlawful.

    You are hereby called upon to {data['demand']} within {data['timeline']} days,
    failing which legal proceedings will be initiated.

    This notice is issued without prejudice to legal rights.
    """
    content.append(Paragraph(body, styles["Normal"]))
    content.append(Spacer(1, 12))

    # Law Sections
    laws = data.get("laws", {})
    law_text = ""
    law_text += format_law_section("IPC", laws.get("ipc"))
    law_text += format_law_section("CrPC", laws.get("crpc"))
    law_text += format_law_section("CPC", laws.get("cpc"))
    law_text += format_law_section("Consumer Law", laws.get("consumer"))

    if law_text:
        content.append(Paragraph("<b>Applicable Legal Provisions:</b><br/>" + law_text, styles["Normal"]))
        content.append(Spacer(1, 12))

    # Disclaimer
    disclaimer = """
    <b>Disclaimer:</b> This AI-generated document is for informational purposes only
    and does not constitute legal advice. Consult a qualified advocate.
    """
    content.append(Paragraph(disclaimer, styles["Normal"]))

    doc.build(content)
    return file_path

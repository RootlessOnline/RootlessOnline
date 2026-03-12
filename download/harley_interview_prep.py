from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak, ListFlowable, ListItem
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily
import os

# Register fonts
pdfmetrics.registerFont(TTFont('Times New Roman', '/usr/share/fonts/truetype/english/Times-New-Roman.ttf'))
registerFontFamily('Times New Roman', normal='Times New Roman', bold='Times New Roman')

# Create document
doc = SimpleDocTemplate(
    "/home/z/my-project/download/Harley_Interview_Prep_Eric_Haas.pdf",
    pagesize=letter,
    title="Harley Interview Prep - Eric Haas",
    author='Z.ai',
    creator='Z.ai',
    subject='Interview preparation materials for meeting with Eric Haas at Primal Nature retreats'
)

# Styles
styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    name='MainTitle',
    fontName='Times New Roman',
    fontSize=28,
    leading=34,
    alignment=TA_CENTER,
    spaceAfter=12
)

subtitle_style = ParagraphStyle(
    name='Subtitle',
    fontName='Times New Roman',
    fontSize=16,
    leading=22,
    alignment=TA_CENTER,
    textColor=colors.HexColor('#666666'),
    spaceAfter=24
)

section_style = ParagraphStyle(
    name='SectionHeader',
    fontName='Times New Roman',
    fontSize=18,
    leading=24,
    spaceBefore=18,
    spaceAfter=12,
    textColor=colors.HexColor('#1F4E79')
)

subsection_style = ParagraphStyle(
    name='SubsectionHeader',
    fontName='Times New Roman',
    fontSize=14,
    leading=18,
    spaceBefore=12,
    spaceAfter=8,
    textColor=colors.HexColor('#2E75B6')
)

body_style = ParagraphStyle(
    name='BodyText',
    fontName='Times New Roman',
    fontSize=11,
    leading=16,
    alignment=TA_LEFT,
    spaceAfter=8
)

body_justify = ParagraphStyle(
    name='BodyJustify',
    fontName='Times New Roman',
    fontSize=11,
    leading=16,
    alignment=TA_JUSTIFY,
    spaceAfter=8
)

quote_style = ParagraphStyle(
    name='QuoteStyle',
    fontName='Times New Roman',
    fontSize=12,
    leading=18,
    alignment=TA_CENTER,
    textColor=colors.HexColor('#1F4E79'),
    spaceBefore=12,
    spaceAfter=12
)

highlight_style = ParagraphStyle(
    name='Highlight',
    fontName='Times New Roman',
    fontSize=12,
    leading=18,
    alignment=TA_LEFT,
    backColor=colors.HexColor('#E8F4F8'),
    borderPadding=8,
    spaceBefore=8,
    spaceAfter=8
)

story = []

# ============= COVER PAGE =============
story.append(Spacer(1, 1.5*inch))
story.append(Paragraph("<b>INTERVIEW PREPARATION</b>", title_style))
story.append(Spacer(1, 12))
story.append(Paragraph("Harley — Regenerative Garden Systems", subtitle_style))
story.append(Spacer(1, 24))
story.append(Paragraph("Meeting with Eric Haas<br/>Primal Nature Retreats", ParagraphStyle(
    name='MeetingInfo',
    fontName='Times New Roman',
    fontSize=14,
    leading=20,
    alignment=TA_CENTER
)))
story.append(Spacer(1, 36))
story.append(Paragraph("Tomorrow at 17:00", ParagraphStyle(
    name='TimeInfo',
    fontName='Times New Roman',
    fontSize=16,
    leading=22,
    alignment=TA_CENTER,
    textColor=colors.HexColor('#C00000')
)))
story.append(Spacer(1, 48))
story.append(Paragraph("<i>\"I build regenerative garden environments that help retreat centers<br/>create deeper nature-based healing experiences.\"</i>", quote_style))

story.append(PageBreak())

# ============= SECTION 1: CORE IDENTITY =============
story.append(Paragraph("<b>1. Core Identity</b>", section_style))
story.append(Spacer(1, 8))

story.append(Paragraph("<b>Remember:</b> You are not asking for a job. You are offering a contribution.", body_style))
story.append(Spacer(1, 8))

# Key phrase box
key_phrase = "\"I like building systems where nature does most of the work.\""
story.append(Paragraph("<b>Key Phrase:</b>", body_style))
story.append(Paragraph(f"<i>{key_phrase}</i>", quote_style))

# ============= SECTION 2: YOUR STORY =============
story.append(Paragraph("<b>2. Your Story (Short Version)</b>", section_style))
story.append(Spacer(1, 8))

story_items = [
    "Grew up helping with dad's landscaping business",
    "Got interested in growing food",
    "Discovered permaculture and passive irrigation",
    "Started experimenting with regenerative systems"
]
for i, item in enumerate(story_items, 1):
    story.append(Paragraph(f"<b>{i}.</b> {item}", body_style))

story.append(Spacer(1, 12))
story.append(Paragraph("<b>Important:</b> Do NOT oversell. Be curious. Frame everything as experiments and ideas.", body_style))
story.append(Paragraph("Example phrase: <i>\"I've been experimenting with...\"</i>", body_style))

# ============= SECTION 3: OLLA EXPLANATION =============
story.append(Paragraph("<b>3. Olla Irrigation Explanation (Simple)</b>", section_style))
story.append(Spacer(1, 8))

olla_text = "\"You bury a porous clay pot in the soil. When the soil dries, it pulls water through the clay. So the plant basically waters itself.\""
story.append(Paragraph(f"<i>{olla_text}</i>", quote_style))

# Benefits
story.append(Paragraph("<b>Benefits to mention:</b>", body_style))
benefits = ["~60-70% water savings (University of Arizona)", "No electricity required", "Extremely low maintenance", "Cheaper than drip irrigation"]
for b in benefits:
    story.append(Paragraph(f"• {b}", body_style))

# ============= SECTION 4: THE INTEGRATION BRIDGE =============
story.append(Paragraph("<b>4. The Integration Bridge — Your Strongest Angle</b>", section_style))
story.append(Spacer(1, 8))

story.append(Paragraph("This is your most powerful connection to Eric's work:", body_style))
story.append(Spacer(1, 6))

bridge_text = "\"I noticed that gardening and nature time are often recommended for psychedelic integration. That made me think gardens could actually be part of the healing environment.\""
story.append(Paragraph(f"<i>{bridge_text}</i>", quote_style))

story.append(Spacer(1, 8))
story.append(Paragraph("<b>Scientific backing:</b>", body_style))
story.append(Paragraph("• The MAPS Integration Workbook specifically recommends gardening as an integration practice", body_style))
story.append(Paragraph("• Horticultural therapy is proven to reduce depression and anxiety", body_style))
story.append(Paragraph("• Nature interaction improves emotional processing", body_style))

# ============= SECTION 5: VALUE PROPOSITION =============
story.append(Paragraph("<b>5. Value Proposition</b>", section_style))
story.append(Spacer(1, 8))

story.append(Paragraph("<b>Full version:</b>", body_style))
full_vp = "\"I build regenerative garden environments that help retreat centers create deeper nature-based healing experiences.\""
story.append(Paragraph(f"<i>{full_vp}</i>", quote_style))

story.append(Spacer(1, 8))
story.append(Paragraph("<b>Shorter version:</b>", body_style))
short_vp = "\"I build garden systems where nature supports healing.\""
story.append(Paragraph(f"<i>{short_vp}</i>", quote_style))

story.append(PageBreak())

# ============= SECTION 6: QUESTIONS TO ASK ERIC =============
story.append(Paragraph("<b>6. Questions to Ask Eric</b>", section_style))
story.append(Spacer(1, 8))

story.append(Paragraph("<i>These questions matter a lot — they show genuine interest:</i>", body_style))
story.append(Spacer(1, 8))

questions = [
    ("1", "How much of the retreat experience happens outdoors?"),
    ("2", "Do guests interact with the land much?"),
    ("3", "Is growing food something you've thought about doing more here?"),
    ("4", "What are the biggest challenges running retreats?"),
    ("5", "What kind of long-term vision do you have for the place?")
]

for num, q in questions:
    story.append(Paragraph(f"<b>{num}.</b> {q}", body_style))
    story.append(Spacer(1, 4))

# ============= SECTION 7: EMERGENCY PHRASES =============
story.append(Paragraph("<b>7. Emergency Phrases (If You Get Stuck)</b>", section_style))
story.append(Spacer(1, 8))

# Create table for emergency phrases
emergency_data = [
    [Paragraph("<b>Situation</b>", ParagraphStyle(name='TableHead', fontName='Times New Roman', fontSize=11, textColor=colors.white, alignment=TA_CENTER)),
     Paragraph("<b>Phrase</b>", ParagraphStyle(name='TableHead', fontName='Times New Roman', fontSize=11, textColor=colors.white, alignment=TA_CENTER))],
    [Paragraph("Conversation stalls", body_style),
     Paragraph("\"I'm curious how you see the land evolving over the next few years.\"", body_style)],
    [Paragraph("Don't know the answer", body_style),
     Paragraph("\"That's a great question — I'd need to experiment with that.\"", body_style)],
    [Paragraph("Talked too much", body_style),
     Paragraph("\"But I'd love to hear how you approach that.\"", body_style)],
    [Paragraph("Things feel awkward", body_style),
     Paragraph("\"I'm still learning a lot, but I really enjoy working with natural systems.\"", body_style)]
]

emergency_table = Table(emergency_data, colWidths=[1.8*inch, 4.5*inch])
emergency_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1F4E79')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ('BACKGROUND', (0, 1), (-1, 1), colors.white),
    ('BACKGROUND', (0, 2), (-1, 2), colors.HexColor('#F5F5F5')),
    ('BACKGROUND', (0, 3), (-1, 3), colors.white),
    ('BACKGROUND', (0, 4), (-1, 4), colors.HexColor('#F5F5F5')),
    ('LEFTPADDING', (0, 0), (-1, -1), 8),
    ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ('TOPPADDING', (0, 0), (-1, -1), 6),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
]))
story.append(emergency_table)

# ============= SECTION 8: OBJECTION HANDLING =============
story.append(Paragraph("<b>8. Handling Objections</b>", section_style))
story.append(Spacer(1, 8))

objections = [
    ("\"We don't have budget for a garden.\"", "\"That's actually why I focus on low-maintenance systems. The idea is to start small and let the system grow over time.\""),
    ("\"We don't need more staff.\"", "\"Totally understandable. I'm mainly looking for a place where I can contribute and learn — even starting small.\""),
    ("\"What's in it for you?\"", "\"I'm looking for a community where I can work with land and build meaningful projects.\"")
]

for obj, resp in objections:
    story.append(Paragraph(f"<b>Objection:</b> {obj}", body_style))
    story.append(Paragraph(f"<b>Response:</b> {resp}", body_style))
    story.append(Spacer(1, 8))

story.append(PageBreak())

# ============= SECTION 9: INTEGRATION GARDEN PLANTS =============
story.append(Paragraph("<b>9. Integration Garden — Key Plants</b>", section_style))
story.append(Spacer(1, 8))

story.append(Paragraph("<i>Only mention a few plants. Too many sounds theoretical.</i>", body_style))
story.append(Spacer(1, 8))

plants_data = [
    [Paragraph("<b>Plant</b>", ParagraphStyle(name='PlantHead', fontName='Times New Roman', fontSize=11, textColor=colors.white, alignment=TA_CENTER)),
     Paragraph("<b>Benefits</b>", ParagraphStyle(name='PlantHead', fontName='Times New Roman', fontSize=11, textColor=colors.white, alignment=TA_CENTER)),
     Paragraph("<b>Connection</b>", ParagraphStyle(name='PlantHead', fontName='Times New Roman', fontSize=11, textColor=colors.white, alignment=TA_CENTER))],
    [Paragraph("Lavender", body_style),
     Paragraph("Reduces anxiety, calming fragrance", body_style),
     Paragraph("Guests can smell plants while walking", body_style)],
    [Paragraph("Chamomile", body_style),
     Paragraph("Relaxation, sleep support", body_style),
     Paragraph("Fresh tea for integration evenings", body_style)],
    [Paragraph("Lemon Balm", body_style),
     Paragraph("Reduces stress, mood support", body_style),
     Paragraph("Gentle herb for nervous system", body_style)],
    [Paragraph("Mint", body_style),
     Paragraph("Refreshing, stimulates senses", body_style),
     Paragraph("Sensory stimulation and fresh tea", body_style)],
    [Paragraph("Rosemary", body_style),
     Paragraph("Improves cognitive clarity", body_style),
     Paragraph("Good for clarity after intense experiences", body_style)]
]

plants_table = Table(plants_data, colWidths=[1.3*inch, 2.3*inch, 2.7*inch])
plants_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1F4E79')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ('BACKGROUND', (0, 1), (-1, 1), colors.white),
    ('BACKGROUND', (0, 2), (-1, 2), colors.HexColor('#F5F5F5')),
    ('BACKGROUND', (0, 3), (-1, 3), colors.white),
    ('BACKGROUND', (0, 4), (-1, 4), colors.HexColor('#F5F5F5')),
    ('BACKGROUND', (0, 5), (-1, 5), colors.white),
    ('LEFTPADDING', (0, 0), (-1, -1), 8),
    ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ('TOPPADDING', (0, 0), (-1, -1), 6),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
]))
story.append(plants_table)

# ============= SECTION 10: BAREFOOT PATH IDEA =============
story.append(Paragraph("<b>10. Bonus Idea: Barefoot Grounding Path</b>", section_style))
story.append(Spacer(1, 8))

story.append(Paragraph("A short path where guests walk barefoot through different textures:", body_style))
story.append(Paragraph("• Grass → Sand → Smooth stones → Wood chips", body_style))
story.append(Spacer(1, 8))
story.append(Paragraph("<b>Purpose:</b> Stimulates sensory nerves and promotes grounding. Used in ecotherapy, mindfulness retreats, and sensory therapy gardens.", body_justify))
story.append(Spacer(1, 8))
story.append(Paragraph("<i>This would be very memorable for retreat guests.</i>", body_style))

# ============= SECTION 11: FINAL REMINDER =============
story.append(Paragraph("<b>11. The Real Goal</b>", section_style))
story.append(Spacer(1, 8))

story.append(Paragraph("<b>The real goal of this interview is NOT the garden.</b>", body_style))
story.append(Spacer(1, 8))
story.append(Paragraph("Eric is deciding: <i>\"Is this someone I want around my retreat?\"</i>", body_style))
story.append(Spacer(1, 8))
story.append(Paragraph("<b>Be:</b>", body_style))
story.append(Paragraph("• Calm — speak slowly and thoughtfully", body_style))
story.append(Paragraph("• Curious — ask genuine questions", body_style))
story.append(Paragraph("• Humble — frame as experiments, not expertise", body_style))
story.append(Paragraph("• Thoughtful — pause before answering", body_style))
story.append(Spacer(1, 8))
story.append(Paragraph("<b>NOT:</b> Overly ambitious, pushy, or selling too hard.", body_style))

story.append(PageBreak())

# ============= SECTION 12: VISUAL MATERIALS =============
story.append(Paragraph("<b>12. Visual Materials — Show on Phone</b>", section_style))
story.append(Spacer(1, 12))

# Add olla irrigation diagram
story.append(Paragraph("<b>Olla Irrigation System Diagram</b>", subsection_style))
story.append(Paragraph("Show this to explain the passive water system:", body_style))
story.append(Spacer(1, 8))

olla_img_path = "/home/z/my-project/download/olla_irrigation_diagram.png"
if os.path.exists(olla_img_path):
    olla_img = Image(olla_img_path, width=5.5*inch, height=5.5*inch)
    story.append(olla_img)

story.append(PageBreak())

# Add garden concept image
story.append(Paragraph("<b>Integration Garden Concept</b>", subsection_style))
story.append(Paragraph("Show this to visualize the retreat garden:", body_style))
story.append(Spacer(1, 8))

garden_img_path = "/home/z/my-project/download/integration_garden_concept.png"
if os.path.exists(garden_img_path):
    garden_img = Image(garden_img_path, width=5.5*inch, height=5.5*inch)
    story.append(garden_img)

# Build PDF
doc.build(story)
print("PDF created successfully!")

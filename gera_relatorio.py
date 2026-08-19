from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

pdf_path = "relatorio_paciente.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=letter)
story = []

styles = getSampleStyleSheet()
title_style = ParagraphStyle(
    "TitleStyle",
    parent=styles["Heading1"],
    fontSize=18,
    spaceAfter=15
)

story.append(Paragraph("Relatório de Análise Genômica - Bioinformática", title_style))
story.append(Paragraph("<b>Amostra:</b> amostra.fastq (Simulada)", styles["Normal"]))
story.append(Paragraph("<b>Referencia:</b> referencia_genoma", styles["Normal"]))
story.append(Spacer(1, 10))

story.append(Paragraph("<b>Resumo dos Achados:</b>", styles["Heading2"]))
story.append(Paragraph("Foi identificada 1 variante genética de impacto moderado no gene <b>ExemploGene</b> (Posição 4: A -> G).", styles["Normal"]))
story.append(Spacer(1, 15))

story.append(Paragraph("<b>Distribuição de Impacto das Variantes:</b>", styles["Heading2"]))
story.append(Image("grafico_mutacoes.png", width=400, height=250))

doc.build(story)
print("Relatório PDF gerado com sucesso como relatorio_paciente.pdf!")

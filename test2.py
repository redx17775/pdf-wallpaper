import fitz
from pprint import pprint
text = "Kleine Schwertwale bilden Schulen"
doc = fitz.open("output.pdf")
page = doc[0]
rl = page.search_for(text)
assert len(rl) == 1
clip = rl[0]
# extract text info now - before the redacting removes it.
blocks = page.get_text("dict", clip=clip)["blocks"]
span = blocks[0]["lines"][0]["spans"][0]
assert span["text"] == text

# remove text
page.add_redact_annot(clip)
page.apply_redactions()

# re-insert same text - different color
font = fitz.Font("figo")  # this must be known somehow - or simply try some font else
tw = fitz.TextWriter(page.rect, color=(1, 0, 0))
# text insertion must use the original insertion poin and font size.
# if not original font, then some fontsize adjustments will probably be required:
# check bbox.width against textlength computed with new font
tw.append(span["origin"], text, font=font, fontsize=span["size"])
tw.write_text(page)
doc.ez_save("x.pdf")
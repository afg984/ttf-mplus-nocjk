import glob
import fontforge


def is_cjk(codepoint):
    if isinstance(codepoint, str):
        codepoint = ord(codepoint)
    return (
        0x4E00 <= codepoint <= 0x9FFF or
        0x3400 <= codepoint <= 0x4DBF or
        0x20000 <= codepoint <= 0x2A6DF or
        0x2A700 <= codepoint <= 0x2B73F or
        0x2B740 <= codepoint <= 0x2B81F or
        0x2B820 <= codepoint <= 0x2CEAF or
        0xF900 <= codepoint <= 0xFAFF or
        0x2F800 <= codepoint <= 0x2FA1F
    )


for filename in glob.glob('*.ttf'):
    font = fontforge.open(filename)

    font.selection.invert()

    for glyph in font.selection.byGlyphs:
        if is_cjk(glyph.encoding):
            font.removeGlyph(glyph)

    font.generate(filename)
    font.close()
    print('processed', filename)

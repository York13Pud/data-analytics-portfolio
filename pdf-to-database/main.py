from pypdf import PdfReader
import tabula

# reader = PdfReader("./pdf-to-database/data/2009_06_08_eos40d.pdf")
# number_of_pages = len(reader.pages)
# page = reader.pages[0]
# text = page.extract_text()


# print(f"Pages: {number_of_pages}")
# print(type(text))


# Read pdf into list of DataFrame
dfs = tabula.read_pdf("pdf-to-database/data/2008_12_08_white_board.pdf", 
                      pages = 'all', 
                      area = (257.709,60.616,436.209,339.522))
                      #area = (163.253,62.847,184.822,337.291))
print(dfs)
# Read remote pdf into list of DataFrame
#dfs2 = tabula.read_pdf("https://github.com/tabulapdf/tabula-java/raw/master/src/test/resources/technology/tabula/arabic.pdf")

# convert PDF into CSV file
#tabula.convert_into("test.pdf", "output.csv", output_format="csv", pages='all')

# convert all PDFs in a directory
#tabula.convert_into_by_batch("input_directory", output_format='csv', pages='all')
import PyPDF2

def f_read_pdf(pdf: str, pagenumber: int) -> str:
    """
    Args:
        pdf (str):          location and name of PDF
        pagenumber (int):   pagenumber to extract text from

    Returns:
        text (str):         extracted text from pagenumber of PDF
    """
    # creating a pdf file object
    pdfFileObj = open(pdf, 'rb')
    
    # creating a pdf reader object
    pdfReader = PyPDF2.PdfReader(pdfFileObj)
    
    # creating a page object
    pageObj = pdfReader.pages[pagenumber]
    
    # extracting text from page
    text = pageObj.extract_text()
    
    # closing the pdf file object
    pdfFileObj.close()

    return text


def f_textual_cleaning(doc) -> str:
    """
    Args:
        doc:                tokenized spacy object of the extracted PDF

    Returns:
        texts (str):         extracted text of doc object
    """
    texts, paragraph = [], []

    for word in doc:
        
        if word.text != '\n' and not word.is_stop and not word.is_punct\
                            and not word.like_num and word.text != 'I':
            paragraph.append(word.lemma_)
            
        if word.text == '\n':
            texts.append(paragraph)
            paragraph = []
            
    return texts
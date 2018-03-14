import io, os
import requests
import tools.pdf2txt as pdf2txt
import re

session = requests.session()


def filter_mock_paper_text(text):
    dirty_strings = [
        "Download more sample papers at – istqbExamCertification.com Download more sample papers at – istqbExamCertification.com ",
        "Download more sample papers at – ",
        "istqbExamCertification.com Download more sample papers at – ",
        "istqbExamCertification.com "
    ]
    for dirty_string in dirty_strings:
        text = text.replace(dirty_string, "")
    return text


for i in range(34-1):
    pdf_mock_test_template = \
        "http://istqbexamcertification.com/{}/{}-{}.pdf"
    pdf_mock_test_url = pdf_mock_test_template.format(
        "wp-content/uploads/2014/09",
        "istqbExamCertification.com-ISTQB-Dumps-and-Mock-Tests-for-Foundation-Level-Paper",
        i + 1
    )
    mock_test_response = session.get(pdf_mock_test_url)  # stream=True
    mock_test_response.raise_for_status()
    mock_test_file = io.BytesIO(mock_test_response.content)
    # The pdfReader variable is a readable object that will be parsed
    path = os.path.dirname(os.path.abspath(__file__)) + '/tmp/'
    file_name = "tmp_{}".format(i)
    pdf_file_path = path + file_name+".pdf"
    txt_file_path = path + file_name+".txt"
    if not os.path.exists(path):
        os.makedirs(path)
    with open(pdf_file_path, "wb") as f:
        f.write(mock_test_response.content)

    s = 'pdf2txt -o%s %s' % (txt_file_path, pdf_file_path)
    pdf2txt.main(s.split(' ')[1:])
    os.remove(pdf_file_path)

    with open(txt_file_path, "r+", encoding="utf-8") as f:
        tmp_text = f.read()
        clean_mock_paper_text = filter_mock_paper_text(tmp_text)
        f.write(clean_mock_paper_text)

        mock_test_pattern = r"(.*)(Answers\s?:)(.*)"
        mock_test_regex = re.compile(mock_test_pattern)
        g = mock_test_regex.findall(clean_mock_paper_text)
        questions_str = next(g.__iter__())[0]
        answers_str = next(g.__iter__())[2]

        # question_pattern = r"(\d+\.)(^(\d+\.))*"
        # questions_regex = re.compile(question_pattern)

        questions_regex = re.compile(r"[0-9]+\.\s")
        split_questions = questions_regex.split(questions_str)

        answer_regex = re.compile(r"[0-9]+")
        split_answers = answer_regex.split(answers_str.strip())
        ia = [next(re.finditer(r"[a|b|c|d]{1}", answer)).group(0) for answer in split_answers if answer.strip() != ""]
        iq = [question for question in split_questions if bool(re.search(r".+a[\)|\.].+b[\)|\.].+c[\)|\.].+d[\)|\.].+", question))]
        # re.match(r".+a\).+b\).+c\).+d\).+", split_questions[0])
        assert len(ia) == len(iq)
        map()


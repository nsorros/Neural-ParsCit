import os
import pytest

@pytest.mark.skipif(os.getenv("CI") == 'true', reason="Not running in CI")
def test_parse(client):
    data = {
        'string': 'Animesh Prasad, Manpreet Kaur and Min-Yen Kan (2018) Neural ParsCit: a deep learning-based reference string parser. International Journal on Digital Libraries. May 2018.'
    }

    assert client.post('/parscit/parse', json=data).status_code == 200

# @pytest.mark.skipif(os.getenv("CI") == 'true', reason="Not running in CI")
# def test_parse_no_content(client):
#     data = {
#         'string': ""
#     }
#
#     assert client.post('/parscit/parse', json=data).status_code == 400

@pytest.mark.skipif(os.getenv("CI") == 'true', reason="Not running in CI")
def test_parse_batch(client):
    data = {
        'strings': ['Animesh Prasad, Manpreet Kaur and Min-Yen Kan (2018) Neural ParsCit: a deep learning-based reference string parser. International Journal on Digital Libraries. May 2018.',
                    'Juyoung An, Namhee Kim, Min-Yen Kan, Muthu Kumar Chandrasekaran and Min Song (2017) Exploring characteristics of highly cited authors according to citation location and content. Journal of the Association for Information Science and Technology. Volume 68, Issue 8 (August). pp. 1975-1988.']
    }

    assert client.post('/parscit/parse/batch', json=data).status_code == 200

@pytest.mark.skipif(os.getenv("CI") == 'true', reason="Not running in CI")
def test_parse_batch_no_content(client):
    data = {
        'strings': []
    }

    assert client.post('/parscit/parse/batch', json=data).status_code == 400

import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message(1, 2)
    with pytest.raises(TypeError):
        encrypt_message("message", "2")
    assert encrypt_message("message", 3) == "sem_egas"
    assert encrypt_message("message", 2) == "egass_em"
    assert encrypt_message("message", -2) == "egassem"

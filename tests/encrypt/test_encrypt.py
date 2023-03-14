import pytest

from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    message = "abcdcb"
    odd_expected_message = "cba_bcd"
    pair_expected_message = "bc_dcba"
    odd_key = 3
    pair_key = 4
    not_valid_index_key = 9

    assert encrypt_message(message, not_valid_index_key) == message[::-1]

    assert encrypt_message(message, odd_key) == odd_expected_message

    assert encrypt_message(message, pair_key) == pair_expected_message

    with pytest.raises(TypeError):
        encrypt_message(odd_key, message)

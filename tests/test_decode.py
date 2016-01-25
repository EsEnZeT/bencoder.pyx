# -*- coding: utf-8 -*-

from bencoder import bdecode


def test_decode_str():
    assert bdecode(b'6:WWWWWW') == b"WWWWWW"


def test_decode_int():
    assert bdecode(b'i233e') == 233


def test_decode_list():
    assert bdecode(b'l1:a1:bi3ee') == [b'a', b'b', 3]


def test_decode_dict():
    od = dict()
    od[b'ka'] = b'va'
    od[b'kb'] = 2
    assert bdecode(b'd2:ka2:va2:kbi2ee') == od


def test_encode_complex():
    od = dict()
    od[b'KeyA'] = [b'listitemA', {b'k': b'v'}, 3]
    od[b'KeyB'] = {b'k': b'v'}
    od[b'KeyC'] = 3
    od[b'KeyD'] = b'AString'
    expected_result = b'd4:KeyAl9:listitemAd1:k1:vei3ee4:KeyBd1:k1:ve4:KeyCi3e4:KeyD7:AStringe'
    assert bdecode(expected_result) == od

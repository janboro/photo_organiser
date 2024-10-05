# Test cases:
# a                 -> a
# a.txt             -> a
# archive.tar.gz    -> archive
# directory/file    -> file
# d.x.y.z/f.a.b.c   -> f
# logs/date.log.txt -> date # Mine!
import unittest

from data_types.file import File


class FileDataclassTest(unittest.TestCase):
    def test1(self) -> None:
        path: str = r"data_types\test\data\test_archive.tar.gz"
        file: File = File(path)
        self.assertEqual(file.path, path)
        self.assertEqual(file.name, "test_archive.tar.gz")
        self.assertEqual(file.content_hash, "250255c0a28a71c28cbbe51ac01766f87b3c6d4facc5b7e44855a8b897631780")
        print("File DataClass Test 1 passed")

    def test2(self) -> None:
        path: str = r"data_types\test\data\test_photo.cr2"
        file: File = File(path)
        self.assertEqual(file.path, path)
        self.assertEqual(file.name, "test_photo.cr2")
        self.assertEqual(file.content_hash, "54e62e1aef2c1f3ab816a8c92829b9ec52a397eaaa2059b02f9c7dcfd7ad7817")
        print("File DataClass Test 2 passed")

    def test3(self) -> None:
        path: str = r"data_types\test\data\test_CONFIG"
        file: File = File(path)
        self.assertEqual(file.path, path)
        self.assertEqual(file.name, "test_CONFIG")
        self.assertEqual(file.content_hash, "311e2b27cd0d05b3baf9ba0bbd109b832c56752ee1e1e7d2183a779c82422f35")
        print("File DataClass Test 3 passed")

    def test4(self) -> None:
        path: str = r"data_types\test\data\.gitignore"
        file: File = File(path)
        self.assertEqual(file.path, path)
        self.assertEqual(file.name, ".gitignore")
        self.assertEqual(file.content_hash, "9023fb6c3ab27775db3c02d7a3877fb168d969b85957458a6be19dc7a8e86c4a")
        print("File DataClass Test 4 passed")

    def run_all_test(self) -> None:
        self.test1()
        self.test2()
        self.test3()
        self.test4()

import pytest

from apilist.aanddbook import AddDeleteBook
from utilities.resultstatus import ResultStatus


class TestAddDelete:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.ad= AddDeleteBook()
        self.rs= ResultStatus()

    def test_addbook(self):
        self.ad.updatedata()
        st = self.ad.validatestatus()
        self.rs.marktest(st, "Status after add book")
        self.ad.updatedata()
        ms = self.ad.validatemessage()
        self.rs.marktest(ms, "Message from add book")
        db = self.ad.validatedb()
        self.rs.marktestfinal(db, "DB update add", "test_addbook")

    def test_deletebook(self):
        self.ad.updatedata()
        dl = self.ad.validatedelete()
        self.rs.marktestfinal(dl, "Delete Book", "test_deletebook")
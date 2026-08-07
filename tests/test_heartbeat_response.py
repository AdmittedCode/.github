import unittest
from scripts.process_heartbeat_response import authority_is_false, make_receipts, select_message

class HeartbeatResponseTests(unittest.TestCase):
    def setUp(self):
        self.authority={"execution":False,"activation":False,"publication":False,"custody":False,"release":False}
        self.message={"message_id":"msg-00000001","exchange_id":"ex-00000001","source_org":"StegVerse-Labs","destination_org":"AdmittedCode","stage":"SENT","detail_class":"AWARENESS","retention_class":"PROJECT","authority":self.authority}
        self.config={"organization":"AdmittedCode","supported_detail_classes":["MEMORY","ACTION","AWARENESS","AUTHORITY","EVIDENCE","BLOCKER","CAPABILITY","CONTEXT"],"response_detail_class":"CAPABILITY"}
    def test_select(self): self.assertEqual(select_message({"messages":[self.message]},"AdmittedCode")["message_id"],"msg-00000001")
    def test_authority_escalation_rejected(self):
        m=dict(self.message); m["authority"]=dict(self.authority,execution=True)
        with self.assertRaises(ValueError): select_message({"messages":[m]},"AdmittedCode")
    def test_received_and_responded(self):
        r,s=make_receipts(self.message,self.config,"2026-08-07T14:42:00Z")
        self.assertEqual((r["stage"],s["stage"]),("RECEIVED","RESPONDED")); self.assertTrue(authority_is_false(r["authority"])); self.assertTrue(authority_is_false(s["authority"])); self.assertFalse(s["classification"]["action_admitted"])
    def test_missing_fails_closed(self):
        with self.assertRaises(ValueError): select_message({"messages":[]},"AdmittedCode")
if __name__=="__main__": unittest.main()

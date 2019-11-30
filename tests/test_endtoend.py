import json
from unittest import TestCase
from solver import Solver


class TestEndToEnd(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_solver(self):
        self.assertDictEqual(Solver('{"a": 3}', '["a"]').start(), {"a": 3})
        self.assertDictEqual(
            Solver('{"a": [1, 2, 3]}', '["a[0]"]').start(),
            {"a[0]": 1}
        )
        self.assertDictEqual(
            Solver('["pedro", "random"]', '["[1]"]').start(),
            {"[1]": 'random'}
        )
        self.assertDictEqual(
            Solver('["pedro", "random"]', '["no_valid_key"]').start(),
            {}
        )
        self.assertDictEqual(
            Solver('["pedro", "random"]', '["[5]"]').start(),
            {}
        )
        self.assertDictEqual(
            Solver('{"pedro": 100, "random": 200}', '["[0]"]').start(),
            {}
        )

    def test_problem(self):
        a = """
                {"guid": "1234", "content": { "type": "text/html", 
                "title": "Challenge 1", "entities": ["1.2.3.4", "wannacry", 
                "malware.com"] }, "score": 74,"time": 1574879179}
            """
        b = '["guid", "content.entities", "score", "score.sign"]'
        self.assertDictEqual(
            Solver(a, b).start(),
            {
                "guid": "1234",
                "content.entities": ["1.2.3.4", "wannacry", "malware.com"],
                "score": 74
            }
        )
        self.assertDictEqual(
            Solver(a, '["guid", "content.entities[0]"]').start(),
            {"guid": "1234", "content.entities[0]": "1.2.3.4"}
        )

    def test_repo(self):
        response_repo = json.dumps({
            "type": "bundle",
            "id": "bundle--bf3c8e50-62a0-440f-9936-279bf4ad34bb",
            "spec_version": "2.0",
            "objects": [
                {
                    "x_mitre_data_sources": [
                        "Process use of network",
                        "Process monitoring",
                        "Process command-line parameters",
                        "Anti-virus",
                        "Binary file metadata"
                    ],
                    "kill_chain_phases": [
                        {
                            "kill_chain_name": "mitre-attack",
                            "phase_name": "defense-evasion"
                        }
                    ],
                    "name": "Indicator Removal from Tools",
                    "description":
                        "If a malicious tool is detected and "
                        "quarantined or otherwise curtailed, "
                        "an adversary may be able to determine why "
                        "the malicious tool was detected (the "
                        "indicator), modify the tool by removing "
                        "the indicator, and use the updated version that is no"
                        " longer detected by the target's defensive systems or"
                        " subsequent targets that may use similar systems.\n\n"
                        "A good example of this is when malware is detected..",
                    "id": "attack-pattern--00d0b012-8a03-"
                          "410e-95de-5826bf542de6",
                    "x_mitre_platforms": [
                        "Linux",
                        "macOS",
                        "Windows"
                    ],
                    "object_marking_refs": [
                        "marking-definition--fa42a846-8d90-4e51-"
                        "bc29-71d5b4802168"
                    ],
                    "x_mitre_version": "1.0",
                    "type": "attack-pattern",
                    "x_mitre_detection":
                        "The first detection of a malicious "
                        "tool may trigger an anti-virus or other security...",
                    "created_by_ref": "identity--c78cb6e5-0c4b-4611-"
                                      "8297-d1b8b55e40b5",
                    "created": "2017-05-31T21:30:54.176Z",
                    "modified": "2018-10-17T00:14:20.652Z",
                    "external_references": [
                        {
                            "external_id": "T1066",
                            "source_name": "mitre-attack",
                            "url": "https://attack.mitre.org/techniques/T1066"
                        }
                    ],
                    "x_mitre_defense_bypassed": [
                        "Log analysis",
                        "Host intrusion prevention systems",
                        "Anti-virus"
                    ]
                }
            ]
        })
        self.assertDictEqual(
            Solver(response_repo, '["id", "objects[0].name", '
                                  '"objects[0].kill_chain_phases"]').start(),
            {
                "id": "bundle--bf3c8e50-62a0-440f-9936-279bf4ad34bb",
                "objects[0].name": "Indicator Removal from Tools",
                "objects[0].kill_chain_phases": [
                    {
                        "kill_chain_name": "mitre-attack",
                        "phase_name": "defense-evasion"
                    }
                ]
            }
        )
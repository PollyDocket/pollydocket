# flake8: noqa

headings = [
    (
        "civil_docket.pdf",
        [
            [
                "DOCKET",
                "CASE INFORMATION",
                "CALENDAR EVENTS",
                "CASE PARTICIPANTS",
                "DISPOSITION SUMMARY",
                "DOCKET ENTRY INFORMATION",
            ]
        ],
    ),
    (
        "cp_criminal_docket.pdf",
        [
            [
                "DOCKET",
                "CASE INFORMATION",
                "STATUS INFORMATION",
                "CALENDAR EVENTS",
                "DEFENDANT INFORMATION",
                "CASE PARTICIPANTS",
                "BAIL INFORMATION",
                "CHARGES",
            ],
            [
                "DOCKET",
                "DISPOSITION SENTENCING/PENALTIES",
                "COMMONWEALTH INFORMATION",
                "ATTORNEY INFORMATION",
                "ENTRIES",
            ],
            ["DOCKET", "ENTRIES"],
        ],
    ),
    (
        "eviction_docket.pdf",
        [
            [
                "DOCKET",
                "CASE INFORMATION",
                "CALENDAR EVENTS",
                "CASE PARTICIPANTS",
                "DISPOSITION SUMMARY",
                "DOCKET ENTRY INFORMATION",
            ]
        ],
    ),
    (
        "misc_docket.pdf",
        [
            [
                "DOCKET",
                "CASE INFORMATION",
                "STATUS INFORMATION",
                "PETITIONER INFORMATION",
                "CASE PARTICIPANTS",
                "COMMONWEALTH INFORMATION",
                "ATTORNEY INFORMATION",
                "ENTRIES",
            ]
        ],
    ),
    (
        "mj_criminal_docket.pdf",
        [
            [
                "DOCKET",
                "CASE INFORMATION",
                "STATUS INFORMATION",
                "CALENDAR EVENTS",
                "DEFENDANT INFORMATION",
                "CASE PARTICIPANTS",
            ],
            ["DOCKET", "BAIL", "CHARGES", "DOCKET ENTRY INFORMATION"],
        ],
    ),
    (
        "non_traffic_docket.pdf",
        [
            [
                "DOCKET",
                "CASE INFORMATION",
                "STATUS INFORMATION",
                "DEFENDANT INFORMATION",
                "CASE PARTICIPANTS",
                "CHARGES",
                "DISPOSITION / SENTENCING DETAILS",
            ],
            [
                "DOCKET",
                "DOCKET ENTRY INFORMATION",
                "PAYMENT PLAN SUMMARY",
                "CASE FINANCIAL INFORMATION",
            ],
        ],
    ),
    (
        "traffic_docket.pdf",
        [
            [
                "DOCKET",
                "CASE INFORMATION",
                "STATUS INFORMATION",
                "DEFENDANT INFORMATION",
                "CASE PARTICIPANTS",
                "CHARGES",
                "DISPOSITION / SENTENCING DETAILS",
            ],
            ["DOCKET", "DOCKET ENTRY INFORMATION", "CASE FINANCIAL INFORMATION"],
        ],
    ),
]

dicts = [
    (
        "civil_docket.pdf",
        {
            "Docket Number": "MJ-49302-CV-0000005-2022",
            "Docket Type": "Civil",
            "Case Information": {
                "Judge Assigned": "The Honorable Kelley Gillette-Walker",
                "Claim Amount": "$8,500.00",
                "Judgment Amount": "",
                "File Date": "01/10/2022",
                "Case Status": "Active",
                "County": "Centre",
            },
            "Calendar Events": [
                {
                    "Event Type": "Civil Action Hearing",
                    "Start Date": "03/04/2022",
                    "Start Time": "11:00 am",
                    "Room": "",
                    "Judge Name": "The Honorable Kelley Gillette-Walker",
                    "Status": "Scheduled",
                }
            ],
            "Case Participants": [
                {
                    "Name": "Austin Gumer",
                    "Type": "Defendant",
                    "Address": "Port Matilda, PA 16870",
                },
                {
                    "Name": "Paul Kensinger",
                    "Type": "Defendant",
                    "Address": "Spring Mills, PA 16875",
                },
                {
                    "Name": "Doug Piertrucha",
                    "Type": "Defendant",
                    "Address": "State College, PA 16803",
                },
                {
                    "Name": "Kyle Crossman",
                    "Type": "Plaintiff",
                    "Address": "Bellefonte, PA 16823",
                },
            ],
            "Disposition Summary": [],
            "Docket Entry Info": [
                {
                    "Filed Date": "01/10/2022",
                    "Entry": "Restricted Certified Civil Complaint",
                    "Filer": "Magisterial District Court 49-3-02",
                    "Applies To": "Austin Gumer, Defendant",
                },
                {
                    "Filed Date": "01/10/2022",
                    "Entry": "Restricted Certified Civil Complaint",
                    "Filer": "Magisterial District Court 49-3-02",
                    "Applies To": "Doug Piertrucha, Defendant",
                },
                {
                    "Filed Date": "01/10/2022",
                    "Entry": "Restricted Certified Civil Complaint",
                    "Filer": "Magisterial District Court 49-3-02",
                    "Applies To": "Paul Kensinger, Defendant",
                },
                {
                    "Filed Date": "01/10/2022",
                    "Entry": "Civil Complaint Filed",
                    "Filer": "Kyle Crossman",
                    "Applies To": "",
                },
            ],
        },
    ),
    (
        "cp_criminal_docket.pdf",
        {
            "Docket Number": "CP-14-CR-0000026-2022",
            "Docket Type": "Criminal",
            "Case Information": {
                "Judge Assigned": "",
                "OTN": "X 355087-5",
                "LOTN": "",
                "Initial Issuing Authority": "Allen W. Sinclair",
                "Arresting Agency": "PSP - Rockview",
                "Complain/Citation No.": "G7018T037K",
                "Case Local Number Type(s)": "",
                "Date Filed": "01/11/2022",
                "Initiation Date": "10/12/2021",
                "Originating Docket No.": "MJ-49303-CR-0000224-2021",
                "Final Issuing Authority": "Allen W. Sinclair",
                "Arresting Officer": "Shane R. Eichelberger",
                "Incident Number": "20201352609",
                "Case Local Number(s)": "",
            },
            "Status Information": {
                "Case Status": "Active",
                "Arrest Date": "09/23/2020",
                "Complaint Date": "10/12/2021",
                "Items": [
                    {"Date": "01/11/2022", "Status": "Awaiting Filing of Information"},
                    {"Date": "01/10/2022", "Status": "Awaiting Pre-Trial Conference"},
                ],
            },
            "Calendar Events": [
                {
                    "Event Type": "Araignment",
                    "Start Date": "02/02/2022",
                    "Start Time": "2:00 pm",
                    "Room": "Courtroom 3",
                    "Judge Name": "Judge Katherine V. Oliver",
                    "Status": "Scheduled",
                }
            ],
            "Defendant Information": {
                "Date Of Birth": "08/23/1994",
                "City/State/Zip": "Bellefonte, PA 16823",
            },
            "Case Participants": [
                {"Name": "Christopher L. Beightol", "Type": "Defendant"}
            ],
            "Bail Information": {
                "Bail": "",
                "Nebbia Status": "None",
                "Items": [
                    {
                        "Bail Action": "Set",
                        "Date": "12/30/2021",
                        "Bail Type": "ROR",
                        "Percentage": "",
                        "Amount": "$0.00",
                        "Posting Status": "",
                        "Posting Date": "",
                    }
                ],
            },
            "Charges": [
                {
                    "Seq.": "1",
                    "Orig Seq.": "1",
                    "Grade": "M",
                    "Statute": "75 § 3802 §§ D2*",
                    "Description": "DUI: Controlled Substance - Impaired Ability - 1st Offense",
                    "Offense Dt.": "09/23/2020",
                    "OTN": "X 355087-5",
                },
                {
                    "Seq.": "2",
                    "Orig Seq.": "2",
                    "Grade": "M",
                    "Statute": "75 § 3802 §§ D1i*",
                    "Description": "DUI: Controlled Substance - Schedule 1 - 1st Offense",
                    "Offense Dt.": "09/23/2020",
                    "OTN": "X 355087-5",
                },
                {
                    "Seq.": "3",
                    "Orig Seq.": "3",
                    "Grade": "M",
                    "Statute": "75 § 3802 §§ D1iii*",
                    "Description": "DUI: Controlled Substance - Metabolite - 1st Offense",
                    "Offense Dt.": "09/23/2020",
                    "OTN": "X 355087-5",
                },
                {
                    "Seq.": "4",
                    "Orig Seq.": "4",
                    "Grade": "S",
                    "Statute": "75 § 4524 §§ E1",
                    "Description": "Improp Sunscreening",
                    "Offense Dt.": "09/23/2020",
                    "OTN": "X 355087-5",
                },
                {
                    "Seq.": "5",
                    "Orig Seq.": "5",
                    "Grade": "S",
                    "Statute": "75 § 3714 §§ A",
                    "Description": "Careless Driving",
                    "Offense Dt.": "09/23/2020",
                    "OTN": "X 355087-5",
                },
            ],
            "Disposition Sentencing/Penalties": "NOT IMPLEMENTED",
            "Commonwealth Info": {
                "Name": "Centre County District Attorney's Office Prosecutor",
                "Supreme Court No.": "",
                "Phone Number(s)": [
                    {
                        "Type": "Phone",
                        "Number": "814-355-6735",
                    }
                ],
                "Address": "Centre County Courthouse\nRoom404\nBellefonte, PA 16823",
            },
            "Attorney Info": {
                "Name": "John William Lhota Private",
                "Supreme Court No.": "319466",
                "Rep. Status": "Active",
                "Phone Number(s)": [
                    {
                        "Type": "Phone",
                        "Number": "814-234-1500",
                    }
                ],
                "Address": "Miler Kistler & Campbell\n720 S Atherton St Ste 201\nState College, PA 16801",
                "Representing": "Christopher L. Beightol",
            },
            "Entries": "NOT IMPLEMENTED",
        },
    ),
    (
        "eviction_docket.pdf",
        {
            "Docket Number": "MJ-49302-LT-0000002-2022",
            "Docket Type": "Landlord/Tenant",
            "Case Information": {
                "Judge Assigned": "The Honorable Kelley Gillette-Walker",
                "Claim Amount": "$0.00",
                "Judgment Amount": "",
                "File Date": "01/10/2022",
                "Case Status": "Active",
                "County": "Centre",
            },
            "Calendar Events": [
                {
                    "Case Calendar Event Type": "Recovery of Real Property Hearing",
                    "Schedule Start Date": "01/25/2022",
                    "Start Time": "1:15 pm",
                    "Room": "",
                    "Judge Name": "The Honorable Kelley Gillette-Walker",
                    "Schedule Status": "Scheduled",
                }
            ],
            "Case Participants": [
                {
                    "Name": "James Richards",
                    "Address": "Julian, PA 16844",
                    "Type": "Defendant",
                },
                {
                    "Name": "Amber Lucas",
                    "Address": "Julian, PA 16844",
                    "Type": "Defendant",
                },
                {
                    "Name": "Arthur John Essy",
                    "Address": "Colorado Springs, CO 80919",
                    "Type": "Plaintiff",
                },
            ],
            "Disposition Summary": {
                "Items": [],
                "Civil Disposition Details": [
                    "Grant possession. No",
                    "Grant possession if money judgement is not satisfied by the time of eviction. No.",
                ],
            },
            "Docket Entry Information": [
                {
                    "Filed Date": "01/13/2022",
                    "Entry": "Landlord/Tenant Complaint Successfully Served",
                    "Filer": "Magisterial District Court 49-3-02",
                    "Applies To": "Amber Lucas, Defendant",
                },
                {
                    "Filed Date": "01/13/2022",
                    "Entry": "Landlord/Tenant Complaint Successfully Served",
                    "Filer": "Magisterial District Court 49-3-02",
                    "Applies To": "James Richards, Defendant",
                },
                {
                    "Filed Date": "01/10/2022",
                    "Entry": "Landlord/Tenant Complaint Issued via Hand Delivery",
                    "Filer": "Magisterial District Court 49-3-02",
                    "Applies To": "Amber Lucas, Defendant",
                },
                {
                    "Filed Date": "01/10/2022",
                    "Entry": "Landlord/Tenant Complaint Issued via Hand Delivery",
                    "Filer": "Magisterial District Court 49-3-02",
                    "Applies To": "James Richards, Defendant",
                },
                {
                    "Filed Date": "01/10/2022",
                    "Entry": "Landlord/Tenant Complaint Filed",
                    "Filer": "Arthur John Essy",
                    "Applies To": "",
                },
            ],
        },
    ),
    (
        "misc_docket.pdf",
        {
            "Docket Number": "CP-14-MD-0000067-2022",
            "Docket Type": "Miscellaneous",
            "Case Information": {
                "Judge Assigned": "",
                "OTN": "",
                "LOTN": "",
                "Initial Issuing Authority": "",
                "Arresting Agency": "",
                "Originating Document No.": "",
                "Case Local Number Type(s)": "",
                "Date Filed": "01/11/2022",
                "Initiation Date": "01/11/2022",
                "Originating Docket No.": "",
                "Final Issuing Authority": "",
                "Arresting Officer": "",
                "Incident Number": "",
                "Case Local Number(s)": "",
            },
            "Status Information": {
                "Case Status": "Closed",
                "Items": [
                    {
                        "Date": "01/11/2022",
                        "Status": "Completed",
                    }
                ],
            },
            "Petitioner Information": {"Date of Birth": "", "City/State/Zip": ""},
            "Case Participants": [{"Name": "Elizabeth J. James", "Type": "Petitioner"}],
            "Commonwealth Information": {"Name": "", "Supreme Court No": ""},
            "Attorney Info": {
                "Name": "",
                "Supreme Court No": "",
                "Rep. Status": "",
                "Phone Number(s)": "",
            },
            "Entries": [
                {
                    "Sequence Number": "1 Coroner's Report-Return of View",
                    "CP Filed Date": "",
                    "Document Date": "",
                    "Filed By": "Centre County Coroner's Office",
                },
                {
                    "Sequence Number": "2 Cremation Authorization",
                    "CP Filed Date": "01/11/2022",
                    "Document Date": "",
                    "Filed By": "Centre County Coroner's Office",
                },
            ],
        },
    ),
    (
        "mj_criminal_docket.pdf",
        {
            "Docket Number": "MJ-493003-CR-0000002-2022",
            "Docket Type": "Criminal",
            "Case Information": {
                "Judge Assigned": "Magisterial District Judge Allen W. Sinclair",
                "OTN": "R 225163-1",
                "Arresting Agency": "Rockview PSP",
                "Complaint No.": "G7018X504K",
                "Disposition": "",
                "County": "Centre",
                "Case Status": "Active",
                "Issue Date": "01/11/2022",
                "File Date": "01/11/2022",
                "Arrest Date": "12/15/2021",
                "Incident No.": "PA 2021-1662169",
                "Disposition Date": "",
                "Township": "Snow Shoe Township",
            },
            "Status Information": {
                "Case Status": "Active",
                "Items": [
                    {
                        "Date": "01/13/2022",
                        "Status": "Awaiting Preliminary Hearing",
                    },
                    {
                        "Date": "01/12/2022",
                        "Status": "Awaiting Preliminary Hearing",
                    },
                    {
                        "Date": "01/11/2022",
                        "Status": "Awaiting Preliminary Hearing",
                    },
                ],
            },
            "Calendar Events": [
                {
                    "Case Calendar Event Type": "Preliminary Arraignment",
                    "Schedule Start Date": "01/13/2022",
                    "Start Time": "10:45 am",
                    "Room": "",
                    "Judge Name": "Magisterial District Judge Allen W. Sinclair",
                    "Schedule Status": "Scheduled",
                },
                {
                    "Case Calendar Event Type": "Preliminary Hearing",
                    "Schedule Start Date": "01/26/2022",
                    "Start Time": "08:30 am",
                    "Room": "",
                    "Judge Name": "Magisterial District Judge Allen W. Sinclair",
                    "Schedule Status": "Scheduled",
                },
            ],
            "Defendant Information": {
                "Name": "Mary L. Hipple",
                "Date of Birth": "12/19/1960",
                "Sex": "Female",
                "Race": "White",
                "Address(es)": [{"Type": "Home", "Address": "Howard, PA 16841"}],
                "Items": [
                    "Advised of His Right to Apply for Assignment of Counsel? No",
                    "Public Defender Requested by the Defendant? No",
                    "Application Provided for Appointment of Public Defender? No",
                    "Has the Defendant Been Fingerprinted? No",
                ],
            },
            "Case Participants": [
                {"Type": "Defendant", "Name": "Mary L. Hipple"},
                {"Type": "Arresting Officer", "Name": "Travis K. Sather"},
            ],
            "Bail": {
                "Bail Set": "",
                "Nebbia Status": "None",
                "Items": [
                    {
                        "Bail Action Type": "Set",
                        "Bail Action Date": "01/13/2022",
                        "Bail Type": "ROR",
                        "Percentage": "",
                        "Amount": "$0.00",
                    }
                ],
            },
            "Charges": [
                {
                    "#": "1",
                    "Charge": "75 § 3802 §§ C**",
                    "Grade": "F3",
                    "Description": "DUI: Highest Rte of Alc (BAC .16+) 2nd Off",
                    "Offense Dt.": "12/15/2021",
                    "Disposition": "",
                },
                {
                    "#": "2",
                    "Charge": "75 § 3802 §§ A1**",
                    "Grade": "M",
                    "Description": "DUI: Gen Imp/Inc of Driving Safely - 2nd Off",
                    "Offense Dt.": "12/15/2021",
                    "Disposition": "",
                },
                {
                    "#": "3",
                    "Charge": "75 § 3714 §§ A ",
                    "Grade": "S",
                    "Description": "Careless Driving",
                    "Offense Dt.": "12/15/2021",
                    "Disposition": "",
                },
                {
                    "#": "4",
                    "Charge": "75 § 3301 §§ A",
                    "Grade": "S",
                    "Description": "Fail To Keep Right",
                    "Offense Dt.": "12/15/2021",
                    "Disposition": "",
                },
                {
                    "#": "5",
                    "Charge": "75 § 3309 §§ 1",
                    "Grade": "S",
                    "Description": "Disregard Traffic Lane (Single)",
                    "Offense Dt.": "12/15/2021",
                    "Disposition": "",
                },
                {
                    "#": "6",
                    "Charge": "75 § 4581 §§ A2II",
                    "Grade": "S",
                    "Description": "Fail to use safety belt - driver and front seat occupant",
                    "Offense Dt.": "12/15/2021",
                    "Disposition": "",
                },
                {
                    "#": "7",
                    "Charge": "75 § 3736 §§ A",
                    "Grade": "S",
                    "Description": "Reckless Driving",
                    "Offense Dt.": "12/15/2021",
                    "Disposition": "",
                },
            ],
            "Docket Entry Information": [
                {
                    "Filed Date": "01/11/2022",
                    "Entry": "First Class Fingerprint Order Issued",
                    "Filer": "Magisterial District Court 49-3-03",
                    "Applies To": "Mary L. Hipple, Defendant",
                },
                {
                    "Filed Date": "01/11/2022",
                    "Entry": "Fingerprint Order Issued",
                    "Filer": "Magisterial District Court 49-3-03",
                    "Applies To": "Mary L. Hipple, Defendant",
                },
                {
                    "Filed Date": "01/11/2022",
                    "Entry": "Criminal Complaint Filed",
                    "Filer": "Magisterial District Court 49-3-03",
                    "Applies To": "",
                },
            ],
        },
    ),
    (
        "non_traffic_docket.pdf",
        {
            "Docket Number": "MJ-49305-NT-0000014-2022",
            "Docket Type": "Non-Traffic",
            "Case Information": {
                "Judge Assigned": "The Honorable Steven Frederic Lachman",
                "OTN": "",
                "Arresting Agency": "Penn State, University PD",
                "Citation No.": "R 3117103-3",
                "Disposition": "Guilty Plea",
                "County": "Centre",
                "Case Status": "Closed",
                "Issue Date": "",
                "File Date": "01/11/2022",
                "Arrest Date": "",
                "Incident No.": "22UP00007",
                "Disposition Date": "01/19/2022",
                "Township": "State College Borough",
            },
            "Status Information": {
                "Case Status": "Closed",
                "Items": [
                    {
                        "Date": "01/19/2022",
                        "Status": "Case Balance Due",
                    },
                    {
                        "Date": "01/19/2022",
                        "Status": "Case Disposed/Penalty Imposed",
                    },
                    {
                        "Date": "01/19/2022",
                        "Status": "Awaiting Sentencing",
                    },
                    {
                        "Date": "01/11/2022",
                        "Status": "Awaiting Plea",
                    },
                ],
            },
            "Defendant Information": {
                "Name": "Yoon-Jae Lee",
                "Date of Birth": "07/31/1999",
                "Sex": "Male",
                "Race": "",
                "Address(es)": [
                    {"Type": "School", "Address": "University Park, PA 16802"}
                ],
            },
            "Case Participants": [
                {"Type": "Defendant", "Name": "Yoon-Jae Lee"},
                {"Type": "Arresting Officer", "Name": "Dale P. Moore"},
            ],
            "Charges": [
                {
                    "#": "1",
                    "Charge": "18 § 3503 §§ B1I",
                    "Grade": "S",
                    "Description": "Def Tres Actual Communication To",
                    "Offense Dt.": "01/04/2022",
                    "Disposition": "Guilty Plea",
                }
            ],
            "Disposition / Sentencing Details": {
                "Case Disposition": "Guilty Plea",
                "Disposition Date": "01/19/2022",
                "Was Defendant Present?": "Yes",
                "Offense Seq./Description": "1 Def Tres Actual Communication To",
                "Offense Disposition": "Guilty Plea",
            },
            "Docket Entry Information": [
                {
                    "Filed Date": "01/19/2022",
                    "Entry": "Summons Cancelled",
                    "Filer": "Magisterial District Court 49-3-05",
                    "Applies To": "Yoon-Jae Lee, Defendant",
                },
                {
                    "Filed Date": "01/19/2022",
                    "Entry": "Guilty Plea",
                    "Filer": "The Honorable Steven Frederic Lachman",
                    "Applies To": "Yoon-Jae Lee, Defendant",
                },
                {
                    "Filed Date": "01/11/2022",
                    "Entry": "Summons Issued",
                    "Filer": "Magisterial District Court 49-3-05",
                    "Applies To": "Yoon-Jae Lee, Defendant",
                },
                {
                    "Filed Date": "01/11/2022",
                    "Entry": "Non-Traffic Citation Filed",
                    "Filer": "Magisterial District Court 49-3-05",
                    "Applies To": "",
                },
                {
                    "Filed Date": "01/11/2022",
                    "Entry": "First Class Summons Issued",
                    "Filer": "Magisterial District Court 49-3-05",
                    "Applies To": "Yoon-Jae Lee, Defendant",
                },
            ],
            "Payment Plan Summary": {
                "Payment Plan No.": "49305-2022-P0000011",
                "Payment Plan Freq.": "Single Payment",
                "Next Due Date": "02/18/2022",
                "Active": "Yes",
                "Next Due Amt.": "$272.25",
                "Overdue Amt.": "$0.00",
                "Responsible Participant": "Yoon-Jae Lee",
                "History": [],
            },
            "Case Financial Information": {
                "Case Balance": "$272.25",
                "Last Payment Amt": "",
                "Next Payment Amt": "",
                "Next Payment Due Date": "",
                "Items": [
                    {
                        "Description": "Crime Victims Compensation (Act 96 of 1984)",
                        "Assessment Amt": "$35.00",
                        "Adjustment Amt": "$0.00",
                        "Non-Monetary Payment Amt": "$0.00",
                        "Payment Amt": "$0.00",
                        "Balance": "$35.00",
                    },
                    {
                        "Description": "Title 18 - Payable to Municipality",
                        "Assessment Amt": "$100.00",
                        "Adjustment Amt": "$0.00",
                        "Non-Monetary Payment Amt": "$0.00",
                        "Payment Amt": "$0.00",
                        "Balance": "$100.00",
                    },
                    {
                        "Description": "Victim Witness Service (Act 111 of 1998)",
                        "Assessment Amt": "$25.00",
                        "Adjustment Amt": "$0.00",
                        "Non-Monetary Payment Amt": "$0.00",
                        "Payment Amt": "$0.00",
                        "Balance": "$25.00",
                    },
                    {
                        "Description": "ATJ",
                        "Assessment Amt": "$6.00",
                        "Adjustment Amt": "$0.00",
                        "Non-Monetary Payment Amt": "$0.00",
                        "Payment Amt": "$0.00",
                        "Balance": "$6.00",
                    },
                    {
                        "Description": "CJES",
                        "Assessment Amt": "$2.50",
                        "Adjustment Amt": "$0.00",
                        "Non-Monetary Payment Amt": "$0.00",
                        "Payment Amt": "$0.00",
                        "Balance": "$2.50",
                    },
                    {
                        "Description": "Commonwealth Cost - HB627 (Act 167 of 1992)",
                        "Assessment Amt": "$9.45",
                        "Adjustment Amt": "$0.00",
                        "Non-Monetary Payment Amt": "$0.00",
                        "Payment Amt": "$0.00",
                        "Balance": "$9.45",
                    },
                    {
                        "Description": "County Court Cost (Act 204 of 1976)",
                        "Assessment Amt": "$35.10",
                        "Adjustment Amt": "$0.00",
                        "Non-Monetary Payment Amt": "$0.00",
                        "Payment Amt": "$0.00",
                        "Balance": "$35.10",
                    },
                    {
                        "Description": "JCPS",
                        "Assessment Amt": "$21.25",
                        "Adjustment Amt": "$0.00",
                        "Non-Monetary Payment Amt": "$0.00",
                        "Payment Amt": "$0.00",
                        "Balance": "$21.25",
                    },
                    {
                        "Description": "Judicial Computer Project",
                        "Assessment Amt": "$8.00",
                        "Adjustment Amt": "$0.00",
                        "Non-Monetary Payment Amt": "$0.00",
                        "Payment Amt": "$0.00",
                        "Balance": "$8.00",
                    },
                    {
                        "Description": "OAG - JCP",
                        "Assessment Amt": "$2.50",
                        "Adjustment Amt": "$0.00",
                        "Non-Monetary Payment Amt": "$0.00",
                        "Payment Amt": "$0.00",
                        "Balance": "$2.50",
                    },
                    {
                        "Description": "State Court Costs (Act 204 of 1976)",
                        "Assessment Amt": "$9.45",
                        "Adjustment Amt": "$0.00",
                        "Non-Monetary Payment Amt": "$0.00",
                        "Payment Amt": "$0.00",
                        "Balance": "$9.45",
                    },
                    {
                        "Description": "Domestic Violence Compensation (Act 44 of 198",
                        "Assessment Amt": "$10.00",
                        "Adjustment Amt": "$0.00",
                        "Non-Monetary Payment Amt": "$0.00",
                        "Payment Amt": "$0.00",
                        "Balance": "$10.00",
                    },
                    {
                        "Description": "Postage - Case",
                        "Assessment Amt": "$8.00",
                        "Adjustment Amt": "$0.00",
                        "Non-Monetary Payment Amt": "$0.00",
                        "Payment Amt": "$0.00",
                        "Balance": "$8.00",
                    },
                ],
            },
        },
    ),
    (
        "traffic_docket.pdf",
        {
            "Docket Number": "MJ-49305-TR-0000080-2022",
            "Docket Type": "Traffic",
            "Case Information": {
                "Judge Assigned": "The Honorable Steven Frederic Lachman",
                "OTN": "",
                "Arresting Agency": "State College Police Department",
                "Citation No.": "E 0008800-1",
                "Disposition": "Guilty Plea",
                "County": "Centre",
                "Case Status": "Closed",
                "Issue Date": "01/12/2022",
                "File Date": "01/12/2022",
                "Arrest Date": "",
                "Incident No.": "",
                "Disposition Date": "01/15/2022",
                "Township": "State College Borough",
            },
            "Status Information": {
                "Case Status": "Closed",
                "Items": [
                    {
                        "Date": "01/18/2022",
                        "Status": "Completed",
                    },
                    {
                        "Date": "01/18/2022",
                        "Status": "Case Balance Due",
                    },
                    {
                        "Date": "01/15/2022",
                        "Status": "Case Disposed/Penalty Imposed",
                    },
                    {
                        "Date": "01/15/2022",
                        "Status": "Awaiting Sentencing",
                    },
                    {
                        "Date": "01/12/2022",
                        "Status": "Awaiting Plea",
                    },
                ],
            },
            "Defendant Information": {
                "Name": "Istiaq Ahmad Rahman",
                "Date of Birth": "06/27/2000",
                "Sex": "Male",
                "Race": "Unknown/Unreported",
                "Address(es)": [{"Type": "Home", "Address": "Lansdale, PA 19446"}],
            },
            "Case Participants": [
                {"Name": "Isitaq Ahmad Rahman", "Type": "Defendant"},
                {
                    "Name": "Scott A. Rusnak",
                    "Type": "Arresting Officer",
                },
            ],
            "Charges": [
                {
                    "#": "1",
                    "Charge": "75 § 3112 §§ A3I",
                    "Grade": "S",
                    "Description": "TRAFFIC-CONTROL-SIGNALS",
                    "Offense Dt.": "01/12/2022",
                    "Disposition": "",
                },
            ],
            "Disposition / Sentencing Details": {
                "Case Disposition": "Guilty Plea",
                "Disposition Date": "01/15/2022",
                "Was Defendant Present?": "No",
                "Offense Seq./Description": "1 Failure to Stop At Red Signal",
                "Offense Disposition": "Guilty Plea",
            },
            "Docket Entry Information": [
                {
                    "Filed Date": "01/15/2022",
                    "Entry": "Guilty Plea",
                    "Filer": "The Honorable Steven Frederic Lachman",
                    "Applies To": "Istiaq Ahmad Rahman, Defendant",
                },
                {
                    "Filed Date": "01/12/2022",
                    "Entry": "Traffic Citation Filed",
                    "Filer": "Magisterial District Court 49-3-05",
                    "Applies To": "",
                },
            ],
            "Case Financial Information": {
                "Case Balance": "$0.00",
                "Last Payment Amt": "",
                "Next Payment Amt": "",
                "Next Payment Due Date": "",
                "Items": [
                    {
                        "Description": "Commonwealth Cost - HB627 (Act 167 of 1992)",
                        "Assessment Amt": "$9.45",
                        "Adjustment Amt": "$0.00",
                        "Non-Monetary Payment Amt": "$0.00",
                        "Payment Amt": "($9.45)",
                        "Balance": "$0.00",
                    },
                    {
                        "Description": "County Court Cost (Act 204 of 1976)",
                        "Assessment Amt": "$23.60",
                        "Adjustment Amt": "$0.00",
                        "Non-Monetary Payment Amt": "$0.00",
                        "Payment Amt": "($23.60)",
                        "Balance": "$0.00",
                    },
                    {
                        "Description": "Emergency Medical Services (Act 45 of 1985)",
                        "Assessment Amt": "$20.00",
                        "Adjustment Amt": "$0.00",
                        "Non-Monetary Payment Amt": "$0.00",
                        "Payment Amt": "($20.00)",
                        "Balance": "$0.00",
                    },
                    {
                        "Description": "JCPS",
                        "Assessment Amt": "$10.00",
                        "Adjustment Amt": "$0.00",
                        "Non-Monetary Payment Amt": "$0.00",
                        "Payment Amt": "($10.00)",
                        "Balance": "$0.00",
                    },
                    {
                        "Description": "Judicial Computer Project",
                        "Assessment Amt": "$8.00",
                        "Adjustment Amt": "$0.00",
                        "Non-Monetary Payment Amt": "$0.00",
                        "Payment Amt": "($8.00)",
                        "Balance": "$0.00",
                    },
                    {
                        "Description": "State Court Costs (Act 204 of 1976)",
                        "Assessment Amt": "$9.45",
                        "Adjustment Amt": "$0.00",
                        "Non-Monetary Payment Amt": "$0.00",
                        "Payment Amt": "($9.45)",
                        "Balance": "$0.00",
                    },
                    {
                        "Description": "Title 75, Motor Vehicle (Morot License Fund)",
                        "Assessment Amt": "$25.00",
                        "Adjustment Amt": "$0.00",
                        "Non-Monetary Payment Amt": "$0.00",
                        "Payment Amt": "($25.00)",
                        "Balance": "$0.00",
                    },
                    {
                        "Description": "ATJ",
                        "Assessment Amt": "$4.00",
                        "Adjustment Amt": "$0.00",
                        "Non-Monetary Payment Amt": "$0.00",
                        "Payment Amt": "($.00)",
                        "Balance": "$0.00",
                    },
                    {
                        "Description": "CAT/MCARE/General Fund",
                        "Assessment Amt": "$45.00",
                        "Adjustment Amt": "$0.00",
                        "Non-Monetary Payment Amt": "$0.00",
                        "Payment Amt": "($45.00)",
                        "Balance": "$0.00",
                    },
                ],
            },
        },
    ),
]

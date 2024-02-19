import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("AccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://registro-ponto-junta-default-rtdb.firebaseio.com/",
})

ref = db.reference('Employees')

data = {
    "000022": {
        "name": "Taiana Vargas",
        "role": "Nutricionista",
        "orgao": "SEAD",
        "last_attendance_time": "2024-01-21 09:15:20",
        "gone_in": "2024-01-21 17:45:00",
        "daily_records": {
            "2024-01-21": {
                "entrance": "2024-01-21 09:15:20",
                "exit": "2024-01-21 17:45:00"
            }
        }
    },
    "00023": {
        "name": "Delciane Pinheiro",
        "role": "Neurologista",
        "orgao": "SEAD",
        "last_attendance_time": "2024-01-21 09:15:20",
        "gone_in": "2024-01-21 17:45:00",
        "daily_records": {
            "2024-01-21": {
                "entrance": "2024-01-21 09:15:20",
                "exit": "2024-01-21 17:45:00"
            }
        }

    },
    "00024": {
        "name": "Altair Ferreira",
        "role": "Cirurgiao",
        "orgao": "SEAD",
        "last_attendance_time": "2024-01-21 09:15:20",
        "gone_in": "2024-01-21 17:45:00",
        "daily_records": {
            "2024-01-21": {
                "entrance": "2024-01-21 09:15:20",
                "exit": "2024-01-21 17:45:00"
            }
        }
    },
    "000025": {
        "name": "Abelardo Passos",
        "role": "Síndico",
        "orgao": "SEAD",
        "last_attendance_time": "2024-01-21 09:15:20",
        "gone_in": "2024-01-21 17:45:00",
        "daily_records": {
            "2024-01-21": {
                "entrance": "2024-01-21 09:15:20",
                "exit": "2024-01-21 17:45:00"
            }
        }
    },
    "00026": {
        "name": "Paulo Victor",
        "role": "Chefe de departamento",
        "orgao": "SEAD",
        "last_attendance_time": "2024-01-21 09:15:20",
        "gone_in": "2024-01-21 17:45:00",
        "daily_records": {
            "2024-01-21": {
                "entrance": "2024-01-21 09:15:20",
                "exit": "2024-01-21 17:45:00"
            }
        }
    },
    "3301": {
        "name": "Joseph Pereira dos Santos",
        "role": "Estagiário",
        "orgao": "SEAD",
        "last_attendance_time": "2024-01-21 09:15:20",
        "gone_in": "2024-01-21 17:45:00",
        "daily_records": {
            "2024-01-21": {
                "entrance": "2024-01-21 09:15:20",
                "exit": "2024-01-21 17:45:00"
            }
        }
    },
    "3302": {
        "name": "Alessandra da Rocha Costa",
        "role": "Aux. Serviços Gerais",
        "orgao": "SEAD",
        "last_attendance_time": "2024-01-21 09:15:20",
        "gone_in": "2024-01-21 17:45:00",
        "daily_records": {
            "2024-01-21": {
                "entrance": "2024-01-21 09:15:20",
                "exit": "2024-01-21 17:45:00"
            }
        }
    },
    "3303": {
        "name": "Bianca Sandrini Lima Pereira",
        "role": "Assessor III",
        "orgao": "SEAD",
        "last_attendance_time": "2024-01-21 09:15:20",
        "gone_in": "2024-01-21 17:45:00",
        "daily_records": {
            "2024-01-21": {
                "entrance": "2024-01-21 09:15:20",
                "exit": "2024-01-21 17:45:00"
            }
        }
    },
    "3304": {
        "name": "Geraldina Pereira Pontes Goes",
        "role": "Aux. Servicos Gerais",
        "orgao": "SEAD",
        "last_attendance_time": "2024-01-21 09:15:20",
        "gone_in": "2024-01-21 17:45:00",
        "daily_records": {
            "2024-01-21": {
                "entrance": "2024-01-21 09:15:20",
                "exit": "2024-01-21 17:45:00"
            }
        }
    },
    "3305": {
        "name": "Arquimedes Carvalho Lamar",
        "role": "Assistente Técnico",
        "orgao": "SEAD",
        "last_attendance_time": "2024-01-21 09:15:20",
        "gone_in": "2024-01-21 17:45:00",
        "daily_records": {
            "2024-01-21": {
                "entrance": "2024-01-21 09:15:20",
                "exit": "2024-01-21 17:45:00"
            }
        }
    },
    "3306": {
        "name": "Eliane Percila de Oliveira Nery",
        "role": "Agente Administrativo",
        "orgao": "SEAD",
        "last_attendance_time": "2024-01-21 09:15:20",
        "gone_in": "2024-01-21 17:45:00",
        "daily_records": {
            "2024-01-21": {
                "entrance": "2024-01-21 09:15:20",
                "exit": "2024-01-21 17:45:00"
            }
        }
    },
    "3307": {
        "name": "Maria do Perpetuo Socorro L. Barros",
        "role": "Aux. Serviços Gerais",
        "orgao": "SEAD",
        "last_attendance_time": "2024-01-21 09:15:20",
        "gone_in": "2024-01-21 17:45:00",
        "daily_records": {
            "2024-01-21": {
                "entrance": "2024-01-21 09:15:20",
                "exit": "2024-01-21 17:45:00"
            }
        }
    },
    "3308": {
        "name": "Lenita Bentes de Magalhaes",
        "role": "Assistente Técnico",
        "orgao": "SEAD",
        "last_attendance_time": "2024-01-21 09:15:20",
        "gone_in": "2024-01-21 17:45:00",
        "daily_records": {
            "2024-01-21": {
                "entrance": "2024-01-21 09:15:20",
                "exit": "2024-01-21 17:45:00"
            }
        }
    },
    "3309": {
        "name": "André Luiz Melo Barbosa",
        "role": "Agente administrativo",
        "orgao": "SEAD",
        "last_attendance_time": "2024-01-21 09:15:20",
        "gone_in": "2024-01-21 17:45:00",
        "daily_records": {
            "2024-01-21": {
                "entrance": "2024-01-21 09:15:20",
                "exit": "2024-01-21 17:45:00"
            }
        }
    },
    "3310": {
        "name": "Raimunda Correa da Silva",
        "role": "Aux. Serviços Gerais",
        "orgao": "SEAD",
        "last_attendance_time": "2024-01-21 09:15:20",
        "gone_in": "2024-01-21 17:45:00",
        "daily_records": {
            "2024-01-21": {
                "entrance": "2024-01-21 09:15:20",
                "exit": "2024-01-21 17:45:00"
            }
        }
    },
    "3311": {
        "name": "Sebastiao Filho F. da Silva",
        "role": "Marinheiro Fluvial",
        "orgao": "SEAD",
        "last_attendance_time": "2024-01-21 09:15:20",
        "gone_in": "2024-01-21 17:45:00",
        "daily_records": {
            "2024-01-21": {
                "entrance": "2024-01-21 09:15:20",
                "exit": "2024-01-21 17:45:00"
            }
        }
    },
    "3313": {
        "name": "Maria Dolores Silva Araújo",
        "role": "Assistente Técnico",
        "orgao": "SEAD",
        "last_attendance_time": "2024-01-21 09:15:20",
        "gone_in": "2024-01-21 17:45:00",
        "daily_records": {
            "2024-01-21": {
                "entrance": "2024-01-21 09:15:20",
                "exit": "2024-01-21 17:45:00"
            }
        }
    },
    "3314": {
        "name": "Heládia Maria Araújo dos Santos",
        "role": "Telefonista",
        "orgao": "SEAD",
        "last_attendance_time": "2024-01-21 09:15:20",
        "gone_in": "2024-01-21 17:45:00",
        "daily_records": {
            "2024-01-21": {
                "entrance": "2024-01-21 09:15:20",
                "exit": "2024-01-21 17:45:00"
            }
        }
    },
    "3315": {
        "name": "Jackson Veiga Frota",
        "role": "Vigia",
        "orgao": "SEAD",
        "last_attendance_time": "2024-01-21 09:15:20",
        "gone_in": "2024-01-21 17:45:00",
        "daily_records": {
            "2024-01-21": {
                "entrance": "2024-01-21 09:15:20",
                "exit": "2024-01-21 17:45:00"
            }
        }
    },
    "3316": {
        "name": "Emerson Lins de Lima",
        "role": "Fiscal Rodoviário",
        "orgao": "SEAD",
        "last_attendance_time": "2024-01-21 09:15:20",
        "gone_in": "2024-01-21 17:45:00",
        "daily_records": {
            "2024-01-21": {
                "entrance": "2024-01-21 09:15:20",
                "exit": "2024-01-21 17:45:00"
            }
        }
    },
    "3317": {
        "name": "Marindia Guerro Dutra",
        "role": "Médica",
        "orgao": "SES",
        "last_attendance_time": "2024-01-21 09:15:20",
        "gone_in": "2024-01-21 17:45:00",
        "daily_records": {
            "2024-01-21": {
                "entrance": "2024-01-21 09:15:20",
                "exit": "2024-01-21 17:45:00"
            }
        }
    },
    "3318": {
        "name": "Allyne Kelly Menezes Batista",
        "role": "Médica",
        "orgao": "SES",
        "last_attendance_time": "2024-01-21 09:15:20",
        "gone_in": "2024-01-21 17:45:00",
        "daily_records": {
            "2024-01-21": {
                "entrance": "2024-01-21 09:15:20",
                "exit": "2024-01-21 17:45:00"
            }
        }
    },
    "3319": {
        "name": "Sandra Maria Kanawatti Lasmar",
        "role": "Médica",
        "orgao": "SES",
        "last_attendance_time": "2024-01-21 09:15:20",
        "gone_in": "2024-01-21 17:45:00",
        "daily_records": {
            "2024-01-21": {
                "entrance": "2024-01-21 09:15:20",
                "exit": "2024-01-21 17:45:00"
            }
        }
    },
    "3320": {
        "name": "Nilufar Zeimarani Nurani",
        "role": "Médica",
        "orgao": "SES",
        "last_attendance_time": "2024-01-21 09:15:20",
        "gone_in": "2024-01-21 17:45:00",
        "daily_records": {
            "2024-01-21": {
                "entrance": "2024-01-21 09:15:20",
                "exit": "2024-01-21 17:45:00"
            }
        }
    },
    "3321": {
        "name": "Mario Jorge Quadros",
        "role": "Médico",
        "orgao": "SES",
        "last_attendance_time": "2024-01-21 09:15:20",
        "gone_in": "2024-01-21 17:45:00",
        "daily_records": {
            "2024-01-21": {
                "entrance": "2024-01-21 09:15:20",
                "exit": "2024-01-21 17:45:00"
            }
        }
    },
    "3322": {
        "name": "Neane Magalhaes de Andrade",
        "role": "Médica",
        "orgao": "SES",
        "last_attendance_time": "2024-01-21 09:15:20",
        "gone_in": "2024-01-21 17:45:00",
        "daily_records": {
            "2024-01-21": {
                "entrance": "2024-01-21 09:15:20",
                "exit": "2024-01-21 17:45:00"
            }
        }
    },
    "3323": {
        "name": "Vicente de Paulo V. Colombo",
        "role": "Marinheiro Fluvial",
        "orgao": "SEAD",
        "last_attendance_time": "2024-01-21 09:15:20",
        "gone_in": "2024-01-21 17:45:00",
        "daily_records": {
            "2024-01-21": {
                "entrance": "2024-01-21 09:15:20",
                "exit": "2024-01-21 17:45:00"
            }
        }
    },
    "3324": {
        "name": "Natasha Lima da Silva Neves",
        "role": "Médica",
        "orgao": "SES",
        "last_attendance_time": "2024-01-21 09:15:20",
        "gone_in": "2024-01-21 17:45:00",
        "daily_records": {
            "2024-01-21": {
                "entrance": "2024-01-21 09:15:20",
                "exit": "2024-01-21 17:45:00"
            }
        }
    }

}
for key, value in data.items():
    ref.child(key).set(value)

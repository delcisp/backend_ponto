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
        "role": "Sindico",
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
        "name": "Joseph Pereira",
        "role": "Estagiario",
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
        "name": "Alessandra Rocha",
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
    "3303": {
        "name": "Bianca Sandrini",
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
        "name": "Geraldina Goes",
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
        "name": "Arquimedes Lamar",
        "role": "Assistente Tecnico",
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
        "name": "Eliane Nery",
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
        "name": "Maria Barros",
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
    "3308": {
        "name": "Lenita Magalhaes",
        "role": "Assistente Tecnico",
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
        "name": "Andre Luiz Barbosa",
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
        "name": "Raimunda Silva",
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
    "3311": {
        "name": "Sebastiao Silva",
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
        "name": "Maria Dolores Araujo",
        "role": "Assistente Tecnico",
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
        "name": "Jackson Frota",
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
        "name": "Emerson Lima",
        "role": "Fiscal Rodoviario",
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
        "name": "Marindia Dutra",
        "role": "Medica",
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
        "name": "Allyne Batista",
        "role": "Medica",
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
        "name": "Sandra Lasmar",
        "role": "Medica",
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
        "name": "Nilufar Nurani",
        "role": "Medica",
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
        "name": "Mario Quadros",
        "role": "Medico",
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
        "name": "Neane Andrade",
        "role": "Medica",
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
        "name": "Vicente Colombo",
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
        "name": "Natasha Neves",
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

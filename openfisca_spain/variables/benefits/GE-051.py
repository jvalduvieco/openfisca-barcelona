from openfisca_core.model_api import *
from openfisca_spain.entities import *

class renda_disponible_inferior_a_530(Variable):
    column = BoolCol
    entity = Person
    definition_period = MONTH
    label = "Available income is under 530 euros/month"
    set_input = set_input_dispatch_by_period

    def formula(person, period, legislation):
        return person('ingressos_disponibles', period) < 530

class cap_familiar_te_renda_disponible_superior_a_530(Variable):
    column = BoolCol
    entity = Household
    definition_period = MONTH
    label = "No one is making more than 530 euros/month"
    set_input = set_input_dispatch_by_period

    def formula(household, period, legislation):
        members_renda_disponible_inferior_a_530 = household.members('renda_disponible_inferior_a_530', period)
        return household.all(members_renda_disponible_inferior_a_530)

class no_se_li_ha_concedit_cap_ajuda_rai_en_els_ultims_12_mesos(Variable):
    column = BoolCol
    entity = Person
    definition_period = MONTH
    label = "The user has not been benefited with a rai in the last 12 months"
    set_input = set_input_dispatch_by_period


class no_se_li_ha_concedit_tres_ajudes_rai_anteiors(Variable):
    column = BoolCol
    entity = Person
    definition_period = MONTH
    label = "The user has been benefited with three consecutive rai benefits"
    set_input = set_input_dispatch_by_period



class treballa_per_compte_propi(Variable):
    column = BoolCol
    entity = Person
    definition_period = MONTH
    label = "The user is iself employed"
    set_input = set_input_dispatch_by_period


class ingressat_en_centre_penitenciari(Variable):
    column = BoolCol
    entity = Person
    definition_period = MONTH
    label = "The user isin prison"
    set_input = set_input_dispatch_by_period


class percep_prestacins_incompatibles_amb_la_feina(Variable):
    column = BoolCol
    entity = Person
    definition_period = MONTH
    label = "The user is up to date with her obligations against the state"
    set_input = set_input_dispatch_by_period


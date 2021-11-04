def get_or_none(classmodel, **kwargs):
    try:
        return classmodel.objects.get(**kwargs)
    except classmodel.DoesNotExist:
        return None


def life_expectancy(persons):
    ages = list()
    average = 0
    for obj in persons:
        if obj.birth and obj.death:
            age = obj.death.year - obj.birth.year
            ages.append(age)
    if ages and len(ages) > 0:
        average = sum(ages)/len(ages)
    return round(average, 2)


def study_duration(persons, Premedical, LicentiateOfPhilosophy):
    durations = list()
    average = 0
    for obj in persons:
        if get_or_none(Premedical, person=obj.pk) and get_or_none(LicentiateOfPhilosophy, person=obj.pk):
            duration = obj.licentiateofphilosophy.date.year - obj.premedical.date.year
            durations.append(duration)
    if len(durations) > 0:
        average = sum(durations)/len(durations)
    return round(average, 2)


def practice_duration(persons, CandidateOfMedicine):
    durations = list()
    average = 0
    for obj in persons:
        if obj.retirement and get_or_none(CandidateOfMedicine, person=obj.pk):
            duration = obj.retirement.year - obj.candidateofmedicine.date.year
            durations.append(duration)
    if len(durations) > 0:
        average = sum(durations)/len(durations)
    return round(average, 2)

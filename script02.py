from script01 import Cat, Session
session = Session()

wanted_catto_ids = [1, 2]
wanted_catto_names = [session.query(Cat).get(x).name for x in wanted_catto_ids]
print(wanted_catto_names)
session.close()

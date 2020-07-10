from __main__ import app
from utils.dbconn import *
from model.discover import *
import json
from flask import jsonify

@app.route('/migration/status')
def migration_status():
    con = create_db_con()
    machines = json.loads(BluePrint.objects.to_json())
    con.close()
    return jsonify(machines)
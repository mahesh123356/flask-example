from flask import Flask,jsonify
application=Flask(__name__)
@application.route("/",methods=["POST","GET"])
def name():
    l1=[]
    for i in range(20):
        if i%2==0:

            l1.append(i)

    return jsonify(l1)
if __name__=="__main__":
    application.run(debug=True)
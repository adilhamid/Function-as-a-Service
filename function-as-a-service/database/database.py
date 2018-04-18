import sys
sys.path.append("..")

from util.mongo_connect import connectMongo

class Database:
	def __init__(self):
		self.collection = connectMongo()

	def insertFunctionEntry(self, functionName, topicName, f):
		f.save("/tmp/" + functionName + '.py')

		self.collection.update({'functionName': functionName, 'topicName': topicName},
                          {'$set':{'path': "/tmp/"}}, True)

	def getDetailsByTopicName(self, topic):
		result = self.collection.find({'topicName': topic})
		return result

	def getAllKafkaTopics(self):
		result = self.collection.distinct("topicName")
		return result

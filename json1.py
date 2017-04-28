#include "rapidjson/writer.h"
#include "rapidjson/stringbuffer.h"
#include <iostream>
using namespace rapidjson;
using namespace std;


	StringBuffer json_string_buffer;
	Writer<StringBuffer> json_writer(json_string_buffer);

	json_writer.StartObject();		//<<<There must be a root object surrounding everything

		json_writer.Key("name1");
		json_writer.Uint(1);
		
		json_writer.Key("name2");
		json_writer.Uint(2);
		

		json_writer.Key("MyArrayOfThings");
		json_writer.StartArray();
		for (i = 0; i< 3; i++)
		{
			json_writer.StartObject();		//<<<If you want to add in more objects you need to put them inside an array
				json_writer.Key("Something");
				json_writer.Uint(1));

				json_writer.Key("SomethingElse");
				json_writer.Uint(2));
			json_writer.EndObject();
		}
		json_writer.EndArray();


	json_writer.EndObject();

	cout << json_string_buffer.GetString() << endl;


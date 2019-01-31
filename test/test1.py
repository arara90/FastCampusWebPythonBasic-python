d ={ "아라": "천재" ,
     "하늘":"천천재",
     "백진":"바보"
}



if "아라" in d:
    print("아라 in d")

if "바보" in d:
    print("바보 in d")
else:
    print("무라고??")


if "바보" in d.values():
    print("바보 in d.value")
else:
    print("노밸류")

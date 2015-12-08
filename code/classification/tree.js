function distance_discretization(distance) {
  if (distance <= 0.1) {
    return 0;
  }
  else if (distance > 0.1 && distance <= 0.2) {
    return 1;
  }
  else if (distance > 0.2 && distance <= 0.3) { 
    return 2;
  }
  else if (distance > 0.3 && distance <= 0.4) {
    return 3;
  }
  else if (distance > 0.4 && distance <= 0.5) {
    return 5;
  }
  else {
    return 6;
  }
}

function velocity_discretization(vel) {
  if (vel <= 5) {
    return 0;
  }
  else if (vel > 5 && vel <= 10 ){
    return 1;
  }
  else if (vel > 10 && vel <= 15) {
    return 2;
  }
  else if (vel > 15 && vel <= 20) {
    return 3;
  }
  else if (vel > 20 && vel <= 25) {
    return 4;
  }
  else if (vel > 25 && vel <= 30) {
    return 5;
  }
  else {
    return 6;
  }
}

function size_discretization(size) {
  if (size <= 5) {
    return 0;
  }
  else if (size > 5 && size <= 10) {
    return 1;
  }
  else if (size > 10 && size <= 15) {
    return 2;
  }
  else if (size > 15 && size <= 20) {
    return 3;
  }
  else if (size > 20 && size <= 25) {
    return 4;
  }
  else if (size > 25 && size <= 30) {
    return 5;
  }
  else {
    return 6;
  }
}

function predict_type(distance, velocity, size) {
  var attributes = {
    '0': distance_discretization(distance),
    '1': velocity_discretization(velocity),
    '2': size_discretization(size)
  };

  while(!tree.value) {
    var rule = tree.rule;
    var operands = rule.split("<=");
    var idx  = parseInt(operands[0].trim());
    var split_value = parseFloat(operands[1].trim());
    if (attributes[idx] <= split_value) {
      tree = tree.left;
    }
    else {
      tree = tree.right;
    }
  }

  return {
    'AMO': tree.value[0],
    'APO': tree.value[1],
    'ATE': tree.value[2],
    'IEO': tree.value[3],
    'ETc': tree.value[4],
    'HTc': tree.value[5],
    'JFc': tree.value[6]
  };
}

var tree = {
  "id": "0", "rule": "1 <= 1.5000", "gini": "0.607448057588", "samples": "245355",
  "left": 
  {
    "id": "1", "rule": "1 <= 0.5000", "gini": "0.644237175989", "samples": "65092",
    "left": 
    {
      "id": "2", "rule": "0 <= 1.5000", "gini": "0.508152390709", "samples": "12958",
      "left": 
      {
        "id": "3", "rule": "0 <= 0.5000", "gini": "0.658219320196", "samples": "5056",
        "left": 
        {
          "id": "4", "criterion": "gini", "impurity": "0.639142218499", "samples": "2498", "value": [567.0, 1147.0, 784.0, 0.0, 0.0, 0.0, 0.0, 0.0]        
        },
        "right": 
        {
          "id": "5", "criterion": "gini", "impurity": "0.636153208044", "samples": "2558", "value": [1178.0, 833.0, 547.0, 0.0, 0.0, 0.0, 0.0, 0.0]        
        }      
      },
      "right": 
      {
        "id": "6", "rule": "0 <= 2.5000", "gini": "0.265104240436", "samples": "7902",
        "left": 
        {
          "id": "7", "criterion": "gini", "impurity": "0.358366517487", "samples": "2992", "value": [2330.0, 550.0, 112.0, 0.0, 0.0, 0.0, 0.0, 0.0]        
        },
        "right": 
        {
          "id": "8", "rule": "0 <= 4.0000", "gini": "0.201221415209", "samples": "4910",
          "left": 
          {
            "id": "9", "criterion": "gini", "impurity": "0.220907399024", "samples": "2820", "value": [2466.0, 338.0, 16.0, 0.0, 0.0, 0.0, 0.0, 0.0]          
          },
          "right": 
          {
            "id": "10", "criterion": "gini", "impurity": "0.173698862206", "samples": "2090", "value": [1890.0, 193.0, 2.0, 3.0, 0.0, 0.0, 2.0, 0.0]          
          }        
        }      
      }    
    },
    "right": 
    {
      "id": "11", "rule": "0 <= 2.5000", "gini": "0.641400680888", "samples": "52134",
      "left": 
      {
        "id": "12", "rule": "0 <= 0.5000", "gini": "0.649408913033", "samples": "33448",
        "left": 
        {
          "id": "13", "criterion": "gini", "impurity": "0.588119709911", "samples": "9120", "value": [1250.0, 4936.0, 2886.0, 48.0, 0.0, 0.0, 0.0, 0.0]        
        },
        "right": 
        {
          "id": "14", "rule": "0 <= 1.5000", "gini": "0.661111093689", "samples": "24328",
          "left": 
          {
            "id": "15", "criterion": "gini", "impurity": "0.652882609673", "samples": "12105", "value": [3113.0, 5198.0, 3762.0, 29.0, 0.0, 0.0, 3.0, 0.0]          
          },
          "right": 
          {
            "id": "16", "criterion": "gini", "impurity": "0.666238889377", "samples": "12223", "value": [3841.0, 4604.0, 3730.0, 37.0, 0.0, 0.0, 11.0, 0.0]          
          }        
        }      
      },
      "right": 
      {
        "id": "17", "rule": "0 <= 4.0000", "gini": "0.575144461986", "samples": "18686",
        "left": 
        {
          "id": "18", "criterion": "gini", "impurity": "0.612256285089", "samples": "9435", "value": [3553.0, 4472.0, 1376.0, 24.0, 0.0, 0.0, 10.0, 0.0]        
        },
        "right": 
        {
          "id": "19", "criterion": "gini", "impurity": "0.526335886162", "samples": "9251", "value": [4126.0, 4843.0, 238.0, 38.0, 0.0, 0.0, 6.0, 0.0]        
        }      
      }    
    }  
  },
  "right": 
  {
    "id": "20", "rule": "1 <= 3.5000", "gini": "0.569572858487", "samples": "180263",
    "left": 
    {
      "id": "21", "rule": "0 <= 2.5000", "gini": "0.611208859406", "samples": "120286",
      "left": 
      {
        "id": "22", "rule": "0 <= 1.5000", "gini": "0.557131144852", "samples": "60639",
        "left": 
        {
          "id": "23", "rule": "0 <= 0.5000", "gini": "0.515361004094", "samples": "32090",
          "left": 
          {
            "id": "24", "rule": "1 <= 2.5000", "gini": "0.462862880204", "samples": "11157",
            "left": 
            {
              "id": "25", "criterion": "gini", "impurity": "0.484644515636", "samples": "7418", "value": [283.0, 4869.0, 2136.0, 73.0, 0.0, 0.0, 57.0, 0.0]            
            },
            "right": 
            {
              "id": "26", "criterion": "gini", "impurity": "0.415908989629", "samples": "3739", "value": [70.0, 2693.0, 953.0, 7.0, 0.0, 0.0, 16.0, 0.0]            
            }          
          },
          "right": 
          {
            "id": "27", "rule": "1 <= 2.5000", "gini": "0.540027120488", "samples": "20933",
            "left": 
            {
              "id": "28", "criterion": "gini", "impurity": "0.557672288843", "samples": "13458", "value": [1461.0, 7886.0, 3972.0, 111.0, 0.0, 0.0, 28.0, 0.0]            
            },
            "right": 
            {
              "id": "29", "criterion": "gini", "impurity": "0.504777351484", "samples": "7475", "value": [385.0, 4710.0, 2310.0, 35.0, 0.0, 0.0, 35.0, 0.0]            
            }          
          }        
        },
        "right": 
        {
          "id": "30", "rule": "1 <= 2.5000", "gini": "0.596425280608", "samples": "28549",
          "left": 
          {
            "id": "31", "criterion": "gini", "impurity": "0.618589457798", "samples": "16691", "value": [3112.0, 8450.0, 5016.0, 97.0, 0.0, 0.0, 16.0, 0.0]          
          },
          "right": 
          {
            "id": "32", "criterion": "gini", "impurity": "0.556848054767", "samples": "11858", "value": [1189.0, 6981.0, 3484.0, 154.0, 0.0, 0.0, 50.0, 0.0]          
          }        
        }      
      },
      "right": 
      {
        "id": "33", "rule": "1 <= 2.5000", "gini": "0.648069481654", "samples": "59647",
        "left": 
        {
          "id": "34", "rule": "0 <= 4.0000", "gini": "0.66312212533", "samples": "27382",
          "left": 
          {
            "id": "35", "criterion": "gini", "impurity": "0.657041754509", "samples": "16474", "value": [4027.0, 6608.0, 5761.0, 69.0, 0.0, 0.0, 9.0, 0.0]          
          },
          "right": 
          {
            "id": "36", "criterion": "gini", "impurity": "0.666446520278", "samples": "10908", "value": [3492.0, 4192.0, 3149.0, 67.0, 0.0, 0.0, 8.0, 0.0]          
          }        
        },
        "right": 
        {
          "id": "37", "rule": "0 <= 4.0000", "gini": "0.627724302625", "samples": "32265",
          "left": 
          {
            "id": "38", "criterion": "gini", "impurity": "0.591928131936", "samples": "15934", "value": [2343.0, 8735.0, 4668.0, 160.0, 2.0, 1.0, 25.0, 0.0]          
          },
          "right": 
          {
            "id": "39", "criterion": "gini", "impurity": "0.648812715423", "samples": "16331", "value": [3432.0, 6748.0, 6028.0, 105.0, 2.0, 0.0, 16.0, 0.0]          
          }        
        }      
      }    
    },
    "right": 
    {
      "id": "40", "rule": "1 <= 5.5000", "gini": "0.452545584004", "samples": "59977",
      "left": 
      {
        "id": "41", "rule": "0 <= 2.5000", "gini": "0.479165770347", "samples": "48461",
        "left": 
        {
          "id": "42", "rule": "1 <= 4.5000", "gini": "0.395303111783", "samples": "15569",
          "left": 
          {
            "id": "43", "rule": "0 <= 0.5000", "gini": "0.424013222402", "samples": "10697",
            "left": 
            {
              "id": "44", "criterion": "gini", "impurity": "0.305875494415", "samples": "1491", "value": [11.0, 1214.0, 263.0, 0.0, 0.0, 0.0, 3.0, 0.0]            
            },
            "right": 
            {
              "id": "45", "rule": "0 <= 1.5000", "gini": "0.440683042622", "samples": "9206",
              "left": 
              {
                "id": "46", "criterion": "gini", "impurity": "0.403801890359", "samples": "3450", "value": [103.0, 2541.0, 793.0, 3.0, 0.0, 0.0, 10.0, 0.0]              
              },
              "right": 
              {
                "id": "47", "criterion": "gini", "impurity": "0.461443381315", "samples": "5756", "value": [335.0, 3958.0, 1437.0, 12.0, 5.0, 0.0, 9.0, 0.0]              
              }            
            }          
          },
          "right": 
          {
            "id": "48", "rule": "0 <= 1.5000", "gini": "0.3232909444", "samples": "4872",
            "left": 
            {
              "id": "49", "rule": "0 <= 0.5000", "gini": "0.306799055339", "samples": "2204",
              "left": 
              {
                "id": "50", "criterion": "gini", "impurity": "0.270730454803", "samples": "641", "value": [11.0, 540.0, 89.0, 0.0, 0.0, 0.0, 1.0, 0.0]              
              },
              "right": 
              {
                "id": "51", "criterion": "gini", "impurity": "0.321098630396", "samples": "1563", "value": [65.0, 1266.0, 227.0, 0.0, 0.0, 0.0, 5.0, 0.0]              
              }            
            },
            "right": 
            {
              "id": "52", "criterion": "gini", "impurity": "0.336350471691", "samples": "2668", "value": [86.0, 2124.0, 453.0, 0.0, 0.0, 0.0, 5.0, 0.0]            
            }          
          }        
        },
        "right": 
        {
          "id": "53", "rule": "1 <= 4.5000", "gini": "0.512017822648", "samples": "32892",
          "left": 
          {
            "id": "54", "rule": "0 <= 4.0000", "gini": "0.53235832603", "samples": "22008",
            "left": 
            {
              "id": "55", "criterion": "gini", "impurity": "0.50620651429", "samples": "8904", "value": [602.0, 5690.0, 2531.0, 61.0, 1.0, 0.0, 19.0, 0.0]            
            },
            "right": 
            {
              "id": "56", "criterion": "gini", "impurity": "0.5487547912", "samples": "13104", "value": [1237.0, 7749.0, 3987.0, 108.0, 0.0, 1.0, 22.0, 0.0]            
            }          
          },
          "right": 
          {
            "id": "57", "rule": "0 <= 4.0000", "gini": "0.466964799082", "samples": "10884",
            "left": 
            {
              "id": "58", "criterion": "gini", "impurity": "0.433830144702", "samples": "4330", "value": [197.0, 3082.0, 1038.0, 6.0, 0.0, 0.0, 7.0, 0.0]            
            },
            "right": 
            {
              "id": "59", "criterion": "gini", "impurity": "0.485135158919", "samples": "6554", "value": [243.0, 4234.0, 2032.0, 32.0, 0.0, 1.0, 11.0, 1.0]            
            }          
          }        
        }      
      },
      "right": 
      {
        "id": "60", "rule": "0 <= 4.0000", "gini": "0.313403729272", "samples": "11516",
        "left": 
        {
          "id": "61", "rule": "0 <= 2.5000", "gini": "0.266712592655", "samples": "5898",
          "left": 
          {
            "id": "62", "rule": "0 <= 1.5000", "gini": "0.244802362752", "samples": "2786",
            "left": 
            {
              "id": "63", "rule": "0 <= 0.5000", "gini": "0.212865866563", "samples": "1142",
              "left": 
              {
                "id": "64", "criterion": "gini", "impurity": "0.179416337625", "samples": "299", "value": [3.0, 270.0, 21.0, 0.0, 0.0, 1.0, 3.0, 1.0]              
              },
              "right": 
              {
                "id": "65", "criterion": "gini", "impurity": "0.224363926495", "samples": "843", "value": [10.0, 738.0, 80.0, 0.0, 2.0, 4.0, 5.0, 4.0]              
              }            
            },
            "right": 
            {
              "id": "66", "criterion": "gini", "impurity": "0.266288679323", "samples": "1644", "value": [51.0, 1397.0, 169.0, 0.0, 8.0, 0.0, 12.0, 7.0]            
            }          
          },
          "right": 
          {
            "id": "67", "criterion": "gini", "impurity": "0.284981719325", "samples": "3112", "value": [62.0, 2594.0, 438.0, 0.0, 3.0, 2.0, 8.0, 5.0]          
          }        
        },
        "right": 
        {
          "id": "68", "criterion": "gini", "impurity": "0.3563508359", "samples": "5618", "value": [89.0, 4361.0, 1135.0, 4.0, 1.0, 4.0, 9.0, 15.0]        
        }      
      }    
    }  
  }
}


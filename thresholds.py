
def get_thresholds():

    _ANGLE_HIP_KNEE_VERT = {
                            'NORMAL' : (0,  32),
                            'TRANS'  : (35, 65),
                            'PASS'   : (70, 95)
                           }    

        
    thresholds = {
                    'HIP_KNEE_VERT': _ANGLE_HIP_KNEE_VERT,

                    'HIP_THRESH'   : [10, 50],
                    'ANKLE_THRESH' : 45,
                    'KNEE_THRESH'  : [50, 70, 95],

                    'OFFSET_THRESH'    : 35.0,
                    'INACTIVE_THRESH'  : 15.0,

                    'CNT_FRAME_THRESH' : 50
                            
                }

    return thresholds

def get_bicep_curl_thresholds():
    # Elbow curl angle: Decreases from 90 (fully extended) towards 0 (fully curled)
    _ANGLE_ELBOW_CURL = {
                          'NORMAL': (15, 30),  # Initial extended position
                          'TRANS': (70, 90),  # Arm halfway bent
                          'PASS': (130, 145)     # Arm fully curled
                        }

    # Shoulder angle thresholds to prevent overextension and maintain alignment
    thresholds = {
                    'ELBOW_CURL': _ANGLE_ELBOW_CURL,
                    
                    'SHOULDER_THRESH': [160],    # Shoulder angle to detect shoulder alignment <70
                    'WRIST_THRESH': [15, 30, 70],    # Elbow angle for different stages of curl
                    
                    'OFFSET_THRESH': 35.0,
                    'INACTIVE_THRESH': 15.0,
                    
                    'CNT_FRAME_THRESH': 50          # Frames to consider for one complete curl
                }

    return thresholds

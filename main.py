# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

OPTIMIZING = 'optmizing'
MODIFYING = 'modifying'
COMPLETED = 'completed'
FAILED = 'failed'

fake_volumes = [
    {
        id: "1",
        volume_type: "gp2"
    },
    {
        id: "2",
        volume_type: "gp2"
    },
    {
        id: "3",
        volume_type: "gp2"
    },
    {
        id: "4",
        volume_type: "gp2"
    }
]

fake_states = {
    "1": "optimizing",
    "2": "modifying",
    "3": "completed",
    "4": "failed"
}

def fake_describe_volumes_modifications(id):
    state = fake_states[id]
    response = {
        "VolumeModifications": [
            {
                "ModificationState": state
            }
        ]
    }

    return response


def fake_get_modification_state(volume_id):
    response = fake_describe_volumes_modifications(volume_id)
    return response


try:
    for v in fake_volumes:
        if v.volume_type == "gp2":
            print(v.id)
            
            # make modify volume call
            
            # print response
            
            while True:
                state = fake_get_modification_state(v.id)
                if state == OPTIMIZING or state == MODIFYING or state == COMPLETED:
                    print('Volume modification initiated for id:' + v.id)
                    break
                elif state == FAILED:
                    print('Volume modify failed for id:' + v.id)
                    break
                else:
                    time.sleep(60)
                
            





#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#region    [import]                                        ┃
#	┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#	region    [from Python import *]                          ┃
import wave
import json
from vosk import Model, KaldiRecognizer
import queue
import sounddevice
#	endregion [from Python import *]                          ┃
#	┣━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━┫
#	region    [from MATRIX import *]                          ┃
from XPRINT import Error
#	endregion [from MATRIX import *]                          ┃
#	┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
#endregion [import]                                        ┃
#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#region    [XVosk] 										   ┃
class XVosk:
    ...
def XVOSK(
    Model = None,

):
    Model = Model(Model)
    WaveOpen = wave.open(
        "Output.wav",
        "rb"
    )

    KaldiR = KaldiRecognizer(
        Model,
        WaveOpen.getframerate()
    )

    #┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    #region    [Process audio] 								   ┃
    while True:
        ReadFrames = WaveOpen.readframes(4000)

        if len(ReadFrames) == 0:
            Error("len(ReadFrames) == 0")
    #endregion [Process audio] 								   ┃
    #┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    while True:
        data = wf.readframes(4000)

        if len(data) == 0:
            break


        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            print(result["text"])

    # Resultado final
    final = json.loads(rec.FinalResult())
    print(final["text"])
#endregion [XVosk] 										   ┃
#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#region    [KeywordDetect()] 							   ┃
def DetectKeyword(
    Keyword,
    ModelPath = "XVOSK_\\Models\\vosk-model-small-es-0.42",
    Function  = None,
):
    Model_ = Model(ModelPath)
    Recognizer = KaldiRecognizer(Model_, 16000)
    AudioQueue = queue.Queue()

    def Callback(Indata, Frames, Time, Status):
        AudioQueue.put(bytes(Indata))

    with sounddevice.RawInputStream(
        samplerate = 16000,
        blocksize=8000,
        dtype="int16",
        channels=1,
        callback=Callback
    ):
        print(f"Keyword {Keyword}: None")
        while True:
            Data = AudioQueue.get()
            if Recognizer.AcceptWaveform(Data):
                Text = json.loads(
                    Recognizer.Result()
                ).get("text", "").lower()
                print(Text)
                if Keyword.lower() in Text:
                    print(f"\033[92mKeyword detect\033[0m")

                    if callable(Function):
                        Function()
                    return
#endregion [KeywordDetect()] 							   ┃
#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
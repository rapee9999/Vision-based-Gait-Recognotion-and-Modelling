# Vision-based-Gait-Recognotion-and-Modelling
Automatic Fourier Modelling of Vision-based Gait Motion for Representing Person


Naturally, people can intuatively understand and recognise human activities through their eyes. Similarly, human activity recognition based on the computer vision have been studied in a number of research for decades. Studies found that there are three separate systems for gait recognition, which are sensor-based, vision-based and floor-based approaches. One of the effective gait analysis is based on signal processing, while gait measure methods usually in vision system. This is considered as a gap of research in this field. To address this problem, the purpose of this research is to automatically generate Fourier models of gait motion, specifically walking, from videoss for representing a person. The methodoly to resolve the research problem was, firstly, to extract gait data, which contains anamotical joint location from videos, and then kinematic parameters were calculated based on the gait data. Lastly, the model of gate motion was fitted with these parameters. The main results were that gait data could be estimated more accurately by trained MPI deep nueral network than COCO model, and resizing images to 368 by 368 pixels is the most effective size. Secondly, Among nine kinematic parameters, there are two gait pattern, which are anlges of inner angle within leg and rotation of leg. Lastly, Fourier modelling with full automatics failed to represent a person’s gait. However, if the Fourier model is fixed angular speed, the model can generate gait signal similar enough to the original gait patterns. There are many technical issue to solve, and overall evaluation is not satisfactory for automatic Fourier modelling from video, but the solution works well with some manual guidline by human.


## Outline
- Presentation for research summary
- Code (GitMo)

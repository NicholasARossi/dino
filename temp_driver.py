
from video_generation import VideoGenerator





if __name__ == '__main__':
    class Arguments:
        input_path='ice2.mp4'
        video_only=False
        #arch='deit_small'
        arch='vit_base'
        patch_size=8
        #pretrained_weights='dino_deitsmall8_pretrain.pth'
        pretrained_weights='dino_vitbase8_pretrain.pth'
        checkpoint_key="teacher"
        output_path='output_0.7'
        resize=None
        threshold=0.6
        video_format='mp4'
        colormap="BlGn"
        fps=24


    vg=VideoGenerator(Arguments)
    vg.run()


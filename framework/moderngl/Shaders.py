import pygame, moderngl
import array

class Shader:
    def __init__(self, custom_uniforms_vert=None, custom_uniforms_frag=None):
        self.R = 1
        self.G = 1
        self.B = 1

        self.ctx = moderngl.create_context()
        self.quad_buffer = self.ctx.buffer(data=array.array('f', [
            # position (x, y), uv coords (x, y)
            -1.0, 1.0, 0.0, 0.0,  # topleft
            1.0, 1.0, 1.0, 0.0,   # topright
            -1.0, -1.0, 0.0, 1.0, # bottomleft
            1.0, -1.0, 1.0, 1.0   # bottomright

            # note
        ]))

        self.custom_uniforms_vert = custom_uniforms_vert
        self.custom_uniforms_frag = custom_uniforms_frag

        self.vert_shader = '''
        #version 330 core
        
        in vec2 vert;
        in vec2 texcoord;
        out vec2 uvs;
        
        void main() {
            uvs = texcoord;
            gl_Position = vec4(vert.x, vert.y, 0.0, 1.0);
        }
        '''

        self.frag_shader = '''
        #version 330 core
        
        uniform sampler2D tex;
        uniform float R;
        uniform float G;
        uniform float B;
        
        in vec2 uvs;
        out vec4 f_color;
        
        void main() {
            vec2 sample_pos = vec2(uvs.x, uvs.y);
            f_color = vec4(texture(tex, sample_pos).r * R, texture(tex, sample_pos).g * G, texture(tex, sample_pos).b * B, 1);
        }
        '''

        self.program = self.ctx.program(vertex_shader=self.vert_shader, fragment_shader=self.frag_shader)
        self.render_object = self.ctx.vertex_array(self.program, [(self.quad_buffer, '2f 2f', 'vert', 'texcoord')])

        self.program["R"] = self.R
        self.program["G"] = self.G
        self.program["B"] = self.B

    def update(self):
        self.program["R"] = self.R
        self.program["G"] = self.G
        self.program["B"] = self.B

    def surf_to_texture(self, surf):
        tex = self.ctx.texture(surf.get_size(), 4)
        tex.filter = (moderngl.NEAREST, moderngl.NEAREST)
        tex.swizzle = 'BGRA'
        tex.write(surf.get_view('1'))
        return tex


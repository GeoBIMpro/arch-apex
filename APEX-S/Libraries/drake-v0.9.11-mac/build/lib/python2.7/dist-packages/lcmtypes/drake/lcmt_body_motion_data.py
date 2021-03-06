"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

import cStringIO as StringIO
import struct

import lcmt_piecewise_polynomial

class lcmt_body_motion_data(object):
    __slots__ = ["timestamp", "body_id", "spline", "in_floating_base_nullspace", "control_pose_when_in_contact", "quat_task_to_world", "translation_task_to_world", "xyz_kp_multiplier", "xyz_damping_ratio_multiplier", "expmap_kp_multiplier", "expmap_damping_ratio_multiplier", "weight_multiplier"]

    def __init__(self):
        self.timestamp = 0
        self.body_id = 0
        self.spline = None
        self.in_floating_base_nullspace = False
        self.control_pose_when_in_contact = False
        self.quat_task_to_world = [ 0.0 for dim0 in range(4) ]
        self.translation_task_to_world = [ 0.0 for dim0 in range(3) ]
        self.xyz_kp_multiplier = [ 0.0 for dim0 in range(3) ]
        self.xyz_damping_ratio_multiplier = [ 0.0 for dim0 in range(3) ]
        self.expmap_kp_multiplier = 0.0
        self.expmap_damping_ratio_multiplier = 0.0
        self.weight_multiplier = [ 0.0 for dim0 in range(6) ]

    def encode(self):
        buf = StringIO.StringIO()
        buf.write(lcmt_body_motion_data._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">qi", self.timestamp, self.body_id))
        assert self.spline._get_packed_fingerprint() == lcmt_piecewise_polynomial.lcmt_piecewise_polynomial._get_packed_fingerprint()
        self.spline._encode_one(buf)
        buf.write(struct.pack(">bb", self.in_floating_base_nullspace, self.control_pose_when_in_contact))
        buf.write(struct.pack('>4d', *self.quat_task_to_world[:4]))
        buf.write(struct.pack('>3d', *self.translation_task_to_world[:3]))
        buf.write(struct.pack('>3d', *self.xyz_kp_multiplier[:3]))
        buf.write(struct.pack('>3d', *self.xyz_damping_ratio_multiplier[:3]))
        buf.write(struct.pack(">dd", self.expmap_kp_multiplier, self.expmap_damping_ratio_multiplier))
        buf.write(struct.pack('>6d', *self.weight_multiplier[:6]))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = StringIO.StringIO(data)
        if buf.read(8) != lcmt_body_motion_data._get_packed_fingerprint():
            raise ValueError("Decode error")
        return lcmt_body_motion_data._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = lcmt_body_motion_data()
        self.timestamp, self.body_id = struct.unpack(">qi", buf.read(12))
        self.spline = lcmt_piecewise_polynomial.lcmt_piecewise_polynomial._decode_one(buf)
        self.in_floating_base_nullspace, self.control_pose_when_in_contact = struct.unpack(">bb", buf.read(2))
        self.quat_task_to_world = struct.unpack('>4d', buf.read(32))
        self.translation_task_to_world = struct.unpack('>3d', buf.read(24))
        self.xyz_kp_multiplier = struct.unpack('>3d', buf.read(24))
        self.xyz_damping_ratio_multiplier = struct.unpack('>3d', buf.read(24))
        self.expmap_kp_multiplier, self.expmap_damping_ratio_multiplier = struct.unpack(">dd", buf.read(16))
        self.weight_multiplier = struct.unpack('>6d', buf.read(48))
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if lcmt_body_motion_data in parents: return 0
        newparents = parents + [lcmt_body_motion_data]
        tmphash = (0xb65ac7cad287a0aa+ lcmt_piecewise_polynomial.lcmt_piecewise_polynomial._get_hash_recursive(newparents)) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if lcmt_body_motion_data._packed_fingerprint is None:
            lcmt_body_motion_data._packed_fingerprint = struct.pack(">Q", lcmt_body_motion_data._get_hash_recursive([]))
        return lcmt_body_motion_data._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)


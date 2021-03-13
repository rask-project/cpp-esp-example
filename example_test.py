from __future__ import print_function

import ttfw_idf


@ttfw_idf.idf_example_test(env_tag='Example_GENERIC')
def test_cpp_rtti_example(env, extra_data):
    dut = env.get_dut('cpp_rtti', 'examples/cxx/rtti', dut_class=ttfw_idf.ESP32DUT)
    dut.start_app()

if __name__ == '__main__':
    test_cpp_rtti_example()

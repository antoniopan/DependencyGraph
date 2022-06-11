import parallel_traverse
import simple_ioc
import sys
import build_config
import dummy_impl


def init(xml_path):
    config = build_config.CreateFromDocument(open(xml_path).read())
    # config = build_config.parallel_buildType()
    simple_ioc.Container().register(config.dependency_parser, lambda: dummy_impl.DummyDependencyExtractor())
    simple_ioc.Container().register(config.graph_parser, lambda: dummy_impl.DummyGraphConverter())
    simple_ioc.Container().register(config.repo_builder, lambda: dummy_impl.DummyRepoBuilder())


if __name__ == '__main__':
    if len(sys.argv) == 1:
        xml_path = 'sample_config.xml'
        init(xml_path)
        bp = parallel_traverse.BuildProcess()
        bp.from_xml(xml_path)
        bp.build()

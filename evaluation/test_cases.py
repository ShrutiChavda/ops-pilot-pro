def test_pipeline(orchestrator):
    r = orchestrator.run()
    assert 'bottlenecks' in r
    assert 'charts' in r
    return 'OK'

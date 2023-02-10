import pytest
from selene import have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


@pytest.mark.usefixtures('demoqa')
class TestFrames:

    def test_frames(self):
        browser.open('frames')
        browser.switch_to.frame(s('iframe#frame1')())
        s('#sampleHeading').should(have.text('sample'))

        browser.switch_to.parent_frame()

        browser.switch_to.frame(s('iframe#frame2')())
        s('#sampleHeading').should(have.text('page'))

        browser.switch_to.parent_frame()

        s('#framesWrapper').should(have.text('switch between'))

    def test_nested_frames(self):
        browser.open('nestedframes')
        browser.switch_to.frame(s('iframe#frame1')())
        s('//body').should(have.text('Parent frame'))

        browser.switch_to.frame(s('iframe[srcdoc]')())
        s('//body').should(have.text('Child Iframe'))

        browser.switch_to.parent_frame()
        browser.switch_to.parent_frame()
        s('#framesWrapper').should(have.text('switch between'))

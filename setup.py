from setuptools import setup, find_packages


setup(
    name='baidu_tts',
    version='0.0.3',
    keywords=('TTS', 'sound', 'Baidu'),
    description='A Python lib of Baidu TTS.',
    url='http://github.com/yetone/baidu_tts',
    license='MIT License',
    author='yetone',
    author_email='yetoneful@gmail.com',
    packages=find_packages(exclude=['tests']),
    platforms='any',
    include_package_data=True,
    tests_require=(
        'pytest',
    ),
    install_requires=['requests>=2.7.0']
)

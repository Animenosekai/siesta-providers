# Specifications

> Siesta Providers Specification v1

## Description

The *Siesta Provider Marketplace* is a way of downloading new providers and extend Siesta functionalities by downloading and installing so-called *providers*.

We will be describing the different specifications of this marketplace in this file.

## Index

- [Description](#description)
- [Index](#index)
- [Creating a provider](#creating-a-provider)
  - [Creating your first provider](#creating-your-first-provider)
  - [Editing your provider](#editing-your-provider)
  - [Tools](#tools)
    - [Console](#console)
    - [Requests](#requests)
    - [Encoder](#encoder)
    - [Exceptions](#exceptions)
    - [Importer](#importer)
    - [Other](#other)
  - [Build Info](#build-info)
    - [Metadata Attributes](#metadata-attributes)
    - [Requirements](#requirements)
    - [Images](#images)
    - [Build Ignore](#build-ignore)
  - [Testing](#testing)
  - [Publishing](#publishing)
- [Builds](#builds)
  - [Build Steps](#build-steps)
- [Official Builds](#official-builds)

## Creating a provider

A provider is something which will expand Siesta abilities and provide users with more features and sources of entertainment.

You can make your own Siesta providers and publish them on this repository to be used by anyone.

### Creating your first provider

To do so, head to your terminal and enter

```bash
# <name of the provider> should be replaced with the name of your new provider a path to the directory you want to create your provider in
siesta provider init <name of the provider>
```

A folder will be created with the needed files.

### Editing your provider

The `__init__.py` file contains the basic structure of your provider.

```python
...
class MyNewProvider(Provider):
    NAME: str = "test"
...
```

You will notice that this file contains a Python class inheriting from `siesta.sdk.providers.models.Provider`.

This is the base class for Siesta providers.

It contains a bunch of default values and things that you will need to modify to make exciting new features.

### Tools

Siesta's Software Development Kit (SDK) comes with a few tools to help you develop your providers.

#### Console

The console lets you log things on the console or in a file (depending on the current server configuration) with different levels of logging.

```python
>>> from siesta.sdk import console
>>> console("Hello world!") # will use the `INFO` level
>>> console.log("Hello world!") # will use the `INFO` level
>>> console.debug("Hello world!") # will use the `DEBUG` level
>>> console.warn("Hello world!") # will use the `WARNING` level
>>> console.error("Hello world!") # will use the `ERROR` level
```

> **Note**
> Please try to use the `DEBUG` level if you need to log something to avoid flooding the end-user console.

#### Requests

Under `siesta.sdk.requests`, there is an extension of the famous `requests` library, which supports easier proxies, caching, exceptions, etc.

You should use the methods declared in this module to provide the end-user the best experience possible, since they will expect Siesta to use their configuration, which affects `siesta.sdk.requests`.

> Example usage

```python
>>> from siesta.sdk.requests import get
>>> get("http://httpbin.org/get")
[200 OK]
```

#### Encoder

You can use all of Siesta's encoder capabilities under the `siesta.sdk.encoder` module.

It provides you with FFmpeg bindings to encode media files, FFprobe bindings to retrieve various information on files, a scene detection script, the *Siesta Media File* implementation.

> Example usage

```python
>>> from siesta.sdk.encoder.ffmpeg import FFmpeg
>>> work = FFmpeg("nyan.mp4", vf="scale=640:480", crf=18, start=2.5)
>>> result = work.run(format="mov") # this will return the video as `bytes`
>>> work.run("nyan_scaled.mp4") # this will output the video to the given directory

>>> from siesta.sdk import console
>>> from siesta.sdk.encoder import Probe
>>> probe = Probe("nyan.mp4")
>>> def test(frame):
...     """
...     Testing out the progress updating
...     
...     The params will be filled automatically by the API
... 
...     Available values : frame, fps, fps_average, bitrate, bitrate_average, total_size, estimated_size, percentage, processed_time, duplicate_frames, dropped_frames, speed, speed_average, elapsed, eta
...     """
...     console.debug(frame, "out of", probe.video.frames, "frames encoded")

>>> result = FFmpeg("nyan.mp4", vf="scale=640:480").run(handler=test)

>>> from siesta.sdk.encoder import Probe
>>> Probe("nyan.mp4")
Probe("c74a01c51f21d0fd2b0cd045ccf50bb3c8147ac1a6b68d348adab9b741542d72", duration=2.446, videos=1, audios=1, subtitles=0)
# it holds lots of informations on the video stream, the audio stream, the subtitles, ...

>>> from siesta.sdk.encoder import media
>>> with open("nyan.media.siesta", "r+b") as f:
...     playlist, data = media.loads(f.read())
>>> media.range("nyan.media.siesta", 129, 1348) # return the bytes from 129 to 1348 excluding the header
>>> media.load_playlist("nyan.media.siesta") # list[media.Fragment]
```

#### Exceptions

The `siesta.sdk.exceptions` module contains different convenient exceptions used throughout Siesta

#### Importer

The `siesta.sdk.importer` is less important but is convenient if you ever need to import a python module dynamically or with an absolute path.

#### Other

You can search up in the source code what tool you might want to use (for example CLI features, etc.)

### Build Info

#### Metadata Attributes

When creating your provider, you can add metadata to your `Provider` class, which will then help the end-user what your new plugin does.

Here are the different fields to add metadata :

| Field | Description | Type | Default |
| ----- | ----------- | ---- | ------- |
| `NAME` | The human-readable name for the provider | `str` | *(the class name)* |
| `DESCRIPTION` | A description of the provider | `str` | `"Welcome to your future provider"` |
| `VERSION` | The version of the provider | `tuple(major: int, minor: int, patch: int, name: str)` | `(1, 0, 0)` |
| `STATUS` | The development status of the provider | `siesta.sdk.providers.Status` | `siesta.sdk.providers.Status.BETA` |
| `AUTHOR` | The author(s) of the provider | `str` | `"Siesta Community"` |
| `LICENSE` | The license used to distribute the provider | `str` | `Status.BETA` |

> **Note**
> About `VERSION` : this attribute can be an integer, which will be treated as `(<int>, 0, 0, "")`

> **Note**
> About `VERSION` : this attribute can be a string, which will be treated as `(0, 0, 0, <str>)`

> **Note**
> About `VERSION` : any attribute can be omitted. Omitted attributes are treated as `0` or `""`

#### Requirements

Sometimes, your provider might need some additional dependencies.

To declare those dependencies, you need to add a `requirements.txt` file in your provider project, just as you would with any *python* project.

#### Images

You can add a logo to your provider by adding one in `images/logo.png`.

You can also add banners as `images/banner1.png`, `images/banner2.png`, etc.

The first banner might appear in the front page of the provider market so choose it wisely!

#### Build Ignore

When using files which aren't needed after the build step, you can add a `.buildignore`, `.siestaignore` or `.gitignore` file to the root of your project to avoid putting those files in the built provider.

This file follows the same syntax as the normal [`.gitignore`](https://git-scm.com/docs/gitignore) files.

For example, we recommend putting the `images` folder in it, to avoid downloading all the logos and banners when installing your provider.

### Testing

You can test your provider by installing it locally.

If you are still in the provider directory, you could return to your terminal and enter :

```bash
# This will install the provider in the current directory
siesta install
```

Or you could provide a path to the project

```bash
siesta install /awesome/path/for/an/awesome/project
```

If you really want to thoroughly debug Siesta, you could use the Siesta Debugging Tools such as `siesta debug`

### Publishing

You can now try publishing your provider by forking this repository and adding your project directory to the `sources` folder.

Try creating a pull request, and we will review your provider before publishing it for everyone to use it.

## Builds

### Build Steps

- Copy the provider in a temporary directory
- Analyze the provider
- Prepare the output directory
- Parse the [*build ignore*](#build-ignore) files
- Archive and compress the provider source code
- Create a hash for the archive
- Bundle the metadata with provider
- Add the file header

## Official Builds

When publishing a provider, a `metadata.siesta.json` file is created with the following TypeScript structure (from the Siesta Website source code) :

```typescript
interface Provider {
    id: string
    name: string
    description: string

    // version control
    version: number[]
    status: "良" | "β" | "α"

    // author control
    author: string
    license: string // generally MIT

    // inside description
    type: ProvideType
    parameters: FunctionParameter[]
    functions: ProviderFunction[]

    requirements: string[]
    build_version: number // the current metadata file version
    hash: string // available at least on official builds
}

interface ProviderFunction {
    name: string
    description: string
    deprecated: boolean
    parameters: FunctionParameter[]
}

interface FunctionParameter {
    name: string
    description: string
    type: string
    optional: boolean
    default?: string
    deprecated: boolean
}

// This describes the type of Provider it exports
interface ProvideType {
    tv: boolean
    media: boolean
    metadata: boolean
}
```

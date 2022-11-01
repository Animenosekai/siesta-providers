# siesta-providers

 A repository of Siesta providers

## Installing a provider

### Using the website

To install a provider, you can head to your server instance and visit [https://\<your-server-instance\>/market](http://localhost:80/market) and install one from there.

### Using the terminal

You can also install a provider to your local instance without having the server instance running by using the command line.

```bash
# using the Provider ID
siesta install <your-provider-id>
```

```bash
# using a direct link
siesta install https://<url>
```

```bash
# using git
siesta install git+https://github.com/Animenosekai/something-something.git
```

## Uploading a provider

You will need to read through the [specifications](./specifications.md) first to have a grasp at how to make your new provider.

To upload a provider, you need to fork this repository, add your new provider to the [`sources`](./sources) folder and make a pull request.

We will then review your provider and build it shortly after it gets accepted.

## Disclaimer

The code of the actual providers are made by the provider maintainers and are not directly associated with this repository.

If you have any claims to make about any of the providers, please open up an [*issue*](https://github.com/Animenosekai/siesta-providers/issues) on this GitHub repository.

## Copyright

- Animenosekai *— Original author —*

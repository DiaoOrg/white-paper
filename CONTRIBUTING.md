# Contributing

[简体中文](CONTRIBUTING.zh-CN.md)

All DiaoOrg members and other contributors are welcome to submit pull requests.

- Keep equivalent English and Chinese documents at matching paths under `docs/en/` and `docs/zh-CN/`. Add, update, rename, and delete both versions in the same PR.
- Keep `README.md` / `README.zh-CN.md` and this guide / its Chinese version synchronized. Shared files use bilingual text where needed.
- Do not add outlines, introductions, sample lessons, or placeholders before content is agreed upon.
- Use relative Markdown links within each language. Keep terminology, commands, references, and conclusions equivalent across translations. Human review must check meaning; CI only checks file pairing and changed paths.
- Submit only material you may share under the [MIT license](LICENSE), and retain attribution for third-party work.

Preview with `python3 -m http.server 8000 --directory docs`. Check both languages and mobile layout. Run `python3 scripts/check_docs.py`; no package installation or build is needed.

Open a PR against `main`, describe the change in English and Chinese, and add your GitHub profile to [CONTRIBUTORS.md](CONTRIBUTORS.md) with your first contribution. Follow the [code of conduct](CODE_OF_CONDUCT.md).

After merge, the site fetches Markdown directly from `main` on navigation or refresh. GitHub may need a short time to serve the new commit. If the live source is unavailable, the site falls back to its last Pages copy. HTML, CSS, JavaScript, and image changes appear after Pages finishes publishing. Unmerged PRs are not shown on the public site.

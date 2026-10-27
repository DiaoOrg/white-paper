# 贡献指南

[English](CONTRIBUTING.md)

欢迎 DiaoOrg 的所有成员及其他贡献者提交 Pull Request。

- 中英文文档分别放在 `docs/en/` 和 `docs/zh-CN/`，保持相同相对路径。新增、修改、重命名和删除必须在同一个 PR 中同步完成。
- `README.md` / `README.zh-CN.md` 及本指南 / 英文版本必须同步维护。共用文件在必要处使用双语文字。
- 在内容确定前，不添加目录大纲、简介、示例课程或占位内容。
- 同一语言内使用相对 Markdown 链接。两种语言的术语、命令、引用和结论须一致。语义一致性由人工审查；CI 只检查文件配对和变更路径。
- 仅提交有权以 [MIT 许可证](LICENSE) 共享的材料，并保留第三方作品的署名。

使用 `python3 -m http.server 8000 --directory docs` 预览，检查中英文与移动端布局。运行 `python3 scripts/check_docs.py` 检查，无需安装依赖或编译。

向 `main` 提交 PR，用中英文简要描述变更，并在首次贡献时将 GitHub 主页加入 [CONTRIBUTORS.md](CONTRIBUTORS.md)。请遵守[行为准则](CODE_OF_CONDUCT.md)。

合并后，网站在切换页面或刷新时直接读取 `main` 中的 Markdown。GitHub 可能需要短暂时间同步新提交；实时源不可用时回退到上次发布的 Pages 副本。HTML、CSS、JavaScript 与图片更新在 Pages 发布完成后生效。未合并的 PR 不会出现在公开站点上。

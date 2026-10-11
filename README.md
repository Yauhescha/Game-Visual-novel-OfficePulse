# OfficePulse

A Russian-language visual novel about a small IT office: relationships, bug reports, salary reviews, technical debt and the choices people make under pressure.

The story is implemented in Ren'Py and follows multiple routes with different endings. The window title is **«Кабинет 2: OfficePulse»**.

## Story systems

- Dialogue choices and branching office scenarios.
- Relationships with developers, QA, management, accounting and DevOps.
- Technical quality, debt, ethics, burnout and other persistent story variables.
- Career, drama, human and absurd routes.
- Custom interface screens, character sprites, backgrounds, music and effects.

## Run the project

1. Install the Ren'Py SDK.
2. Place or clone this repository inside the launcher's configured projects directory.
3. Select the project in the Ren'Py launcher and choose **Launch Project**.

The repository does not pin a Ren'Py SDK version. Use an SDK compatible with the checked-in scripts and review any launcher migration messages before replacing project files.

For a desktop distribution, use **Build Distributions** in the launcher. Android packaging requires Ren'Py's Android tooling and a local signing configuration; `android.json` contains the application settings.

## Source layout

| Path | Purpose |
| --- | --- |
| `game/script.rpy` | Story entry point |
| `game/routes/` | Acts, routes and endings |
| `game/variables.rpy` | Relationships, story metrics and flags |
| `game/characters.rpy`, `game/images.rpy` | Characters and image definitions |
| `game/screens*.rpy` | Standard and custom UI |
| `game/options.rpy` | Window and application configuration |

## Extend the story

Add route labels under `game/routes/`, define new state with Ren'Py `default` statements, and connect scenes through menus and jumps. Keep variable names consistent with the conditions in `endings.rpy`.

Run Ren'Py's **Check Script (Lint)** after editing dialogue or route transitions. Review `ASSET_LIST.txt` when working with the included artwork and audio.

This repository is archived and preserves the current novel project.

{
  description = "playground python";

  inputs = {
    flake-parts.url = "github:hercules-ci/flake-parts";
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    treefmt-nix.url = "github:numtide/treefmt-nix";
    devenv.url = "github:cachix/devenv";
  };

  outputs =
    inputs@{ flake-parts, ... }:
    flake-parts.lib.mkFlake { inherit inputs; } {
      imports = [
        inputs.treefmt-nix.flakeModule
        inputs.devenv.flakeModule
      ];
      systems = [
        "x86_64-linux"
        "aarch64-linux"
        "aarch64-darwin"
        "x86_64-darwin"
      ];
      perSystem =
        {
          config,
          # self',
          # inputs',
          pkgs,
          # system,
          ...
        }:
        {
          devenv = {
            shells.default = {
              scripts = {
                list =
                  let
                    inherit (pkgs) lib;
                  in
                  {
                    exec = ''
                      echo
                      echo 🦾 Helper scripts you can run to make your development richer:
                      echo 🦾
                      ${pkgs.gnused}/bin/sed -e 's| |••|g' -e 's|=| |' <<EOF \
                      | ${pkgs.util-linuxMinimal}/bin/column -t | ${pkgs.gnused}/bin/sed -e 's|^|🦾 |' -e 's|••| |g'
                      ${lib.generators.toKeyValue { } (
                        lib.mapAttrs (name: value: value.description) config.devenv.shells.default.scripts
                      )}
                      EOF
                      echo
                    '';
                    description = "devenvで定義したのscripts一覧";
                  };
              };
              packages = with pkgs; [
                pyright
                ruff
                python313Full
                python313Packages.uv
              ];
            };
          };
        };
    };
}

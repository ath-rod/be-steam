##
# Opens API Reference
cd docs && \
yarn install && \
npx @redocly/cli preview-docs api-reference.yaml -p 5001 && \
cd ..


# LegacyLens roadmap

## MVP (included)
- Upload source files to local API
- Extract basic program, job, copybook, table and dataset references
- Render dependency graph
- Analyze reverse dependencies for a changed component
- Look up curated DB2/zOS/JCL errors

## Next iteration
1. Persist projects and analysis results (SQLite locally, DynamoDB on AWS)
2. Replace regex-only parser with COBOL/JCL-aware tokenization and fixtures
3. Add source code explorer with Monaco
4. Add test-case generation from deterministic impact results
5. Add authenticated S3 presigned upload and asynchronous analysis workflow
6. Add Bedrock/Strands agent with retrieval-backed error explanations
7. Deploy frontend to Vercel and API to AWS

# used for finding output groups of a specific target
# (e.g. to later be able to select a specific file (or set of files))
# see https://stackoverflow.com/a/61282031

def _output_group_query_aspect_impl(target, ctx):
  for og in target.output_groups:
    print("output group " + str(og) + ": " + str(getattr(target.output_groups, og)))
  return []

output_group_query_aspect = aspect(
    implementation = _output_group_query_aspect_impl,
)